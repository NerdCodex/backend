from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS with specific origins
CORS(app, resources={r"/image/*": {"origins": "*"}})

@app.route('/image/<path:filename>')
def serve_image(filename):
    try:
        return send_from_directory('static/images', filename)
    except FileNotFoundError:
        return "Image not found", 404


if __name__ == '__main__':
    app.run(host='192.168.230.72', port=5000, debug=True)
