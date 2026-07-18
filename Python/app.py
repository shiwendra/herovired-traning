from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-super-secure-secret-key'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 1. FLASK-LOGIN SETUP
login_manager = LoginManager()
login_manager.login_view = 'login'  # Redirects unauthenticated users here
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 2. DATABASE MODEL (Authentication & Authorization Roles)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), default='user')  # Roles: 'user', 'admin'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# 3. AUTHORIZATION DECORATOR (RBAC)
def role_required(required_role):
    def decorator(f):
        @wraps(f)
        @login_required  # Ensures user is authenticated first
        def decorated_function(*args, **kwargs):
            if current_user.role != required_role:
                abort(403)  # HTTP Forbidden
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# 4. AUTHENTICATION ROUTES
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role', 'user')  # Default to standard user

        if User.query.filter_by(username=username).first():
            return "Username already exists!", 400

        new_user = User(username=username, role=role)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return '''
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            Role: <select name="role"><option value="user">User</option><option value="admin">Admin</option></select><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        
        return "Invalid credentials", 401
        
    return '''
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# 5. PROTECTED ROUTES (Authorization Examples)
@app.route('/dashboard')
@login_required  # Anyone logged in can access
def dashboard():
    return f"Welcome to your Dashboard, {current_user.username}! Your role is: {current_user.role}. <a href='/logout'>Logout</a>"

@app.route('/admin')
@role_required('admin')  # ONLY admins can access
def admin_panel():
    return "Welcome to the strictly restricted Admin Panel!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
