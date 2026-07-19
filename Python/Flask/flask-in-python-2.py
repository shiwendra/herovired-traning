from flask import Flask, jsonify, request 

app = Flask(__name__)
@app.route('/home', methods=['get'])
def home():
    return jsonify({"Success": True, "message": "Welcome to the home page!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "Success": True,
        "message": "Hello, World!"
               })

if __name__ == '__main__':
    app.run(debug=True)