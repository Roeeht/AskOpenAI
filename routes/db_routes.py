from flask import Blueprint, jsonify, request
from models.questions_model import Qa, db

qa_bp = Blueprint('qa_bp', __name__)

@qa_bp.route('/qa', methods=['POST'])
def create_qa():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({"error": "question is required"}), 400

    try:
        new_qa = Qa(data['question'], data['answer'])
        db.session.add(new_qa)
        db.session.commit()
        return jsonify(new_qa.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@qa_bp.route('/history', methods=['GET'])
def get_history():
    history = Qa.query.all()
    return jsonify([question.to_dict() for question in history]), 200




