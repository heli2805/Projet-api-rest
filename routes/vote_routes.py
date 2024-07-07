# routes/vote_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import get_db

vote_bp = Blueprint('vote_bp', __name__)

@vote_bp.route('/votes', methods=['POST'])
@jwt_required()
def create_vote():
    data = request.get_json()
    voteValue = data.get('voteValue')
    promptID = data.get('promptID')
    userID = get_jwt_identity()

    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO "Vote" (voteValue, userID, promptID)
    VALUES (%s, %s, %s) RETURNING voteID
    ''', (voteValue, userID, promptID))

    voteID = cur.fetchone()[0]
    conn.commit()
    cur.close()

    return jsonify({"voteID": voteID}), 201
