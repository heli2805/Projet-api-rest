# routes/user_routes.py

from flask import Blueprint, request, jsonify
from models import get_db, hash_password

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    login = data.get('login')
    password = hash_password(data.get('password'))
    role = data.get('role')
    groupID = data.get('groupID')

    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO "User" (firstname, lastname, login, password, role, groupID)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING userID
    ''', (firstname, lastname, login, password, role, groupID))

    userID = cur.fetchone()[0]
    conn.commit()
    cur.close()

    return jsonify({"userID": userID}), 201
