from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Dummy user database
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Check credentials
    if username in users_db and users_db[username] == password:
        return jsonify({"msg": "login successful"}), 200
    return jsonify({'msg': 'Invalid username or password'}), 401

@app.route('/register', methods=['POST'])
def register():
    name = request.json.get('name')
    college = request.json.get('college_name')
    username = request.json.get('username')
    password = request.json.get('password')

    users_db[username] = password
    print(name, college, username, password)

    return jsonify({"msg": "registeration successful"}), 200

@app.route('/image/<path:filename>')
def serve_image(filename):
    try:
        return send_from_directory('static/images', filename)
    except FileNotFoundError:
        return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True)
