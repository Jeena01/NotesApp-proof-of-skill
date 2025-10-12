from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
CORS(app)

users = {}
notes = {}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            token = token.split()[1]  # Bearer <token>
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    if username in users:
        return jsonify({"message": "User already exists"}), 400
    users[username] = generate_password_hash(password)
    notes[username] = []
    return jsonify({"message": "User registered successfully"})

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    if username not in users or not check_password_hash(users[username], password):
        return jsonify({"message": "Invalid credentials"}), 401
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
                       app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({"token": token})

# Notes endpoints
@app.route('/notes', methods=['GET'])
@token_required
def get_notes(current_user):
    return jsonify(notes[current_user])

@app.route('/notes', methods=['POST'])
@token_required
def add_note(current_user):
    data = request.json
    note = {"id": len(notes[current_user]) + 1, "text": data['text']}
    notes[current_user].append(note)
    return jsonify(note), 201

@app.route('/notes/<int:note_id>', methods=['DELETE'])
@token_required
def delete_note(current_user, note_id):
    notes[current_user] = [n for n in notes[current_user] if n['id'] != note_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
