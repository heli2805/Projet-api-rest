# routes/note_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import get_db

note_bp = Blueprint('note_bp', __name__)

@note_bp.route('/notes', methods=['POST'])
@jwt_required()
def create_note():
    data = request.get_json()
    noteValue = data.get('noteValue')
    promptID = data.get('promptID')
    userID = get_jwt_identity()

    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO "Note" (noteValue, userID, promptID)
    VALUES (%s, %s, %s) RETURNING noteID
    ''', (noteValue, userID, promptID))

    noteID = cur.fetchone()[0]
    conn.commit()
    cur.close()

    return jsonify({"noteID": noteID}), 201


