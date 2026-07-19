from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# 1. Standard Text Route
@app.route('/')
def home():
    return "Hello, World! Your Flask app is running."

# 2. JSON API Route (Accepts GET requests)
@app.route('/api/greet', methods=['GET'])
def greet_user():
    # Get the 'name' parameter from the URL query string (defaults to 'Guest')
    user_name = request.args.get('name', 'Guest')
    return jsonify({
        "status": "success",
        "message": f"Welcome to Flask, {user_name}!"
    })

# 3. Dynamic URL Route
@app.route('/user/<username>')
def show_user_profile(username):
    return f"Viewing profile for user: {username}"

# Run the local development server
if __name__ == '__main__':
    app.run(debug=True)
