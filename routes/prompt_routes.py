# routes/prompt_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import get_db

prompt_bp = Blueprint('prompt_bp', __name__)

@prompt_bp.route('/prompts', methods=['POST'])
@jwt_required()
def create_prompt():
    data = request.get_json()
    content = data.get('content')
    userID = get_jwt_identity()

    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO "Prompt" (content, status, userID)
    VALUES (%s, %s, %s) RETURNING promptID
    ''', (content, 'En attente', userID))

    promptID = cur.fetchone()[0]
    conn.commit()
    cur.close()

    return jsonify({"promptID": promptID}), 201
