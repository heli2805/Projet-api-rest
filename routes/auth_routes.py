# routes/auth_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "User" WHERE login=%s', (login,))
    user = cur.fetchone()

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=user['userID'])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401
