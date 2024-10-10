from flask import Blueprint, jsonify, request
from models.questions_model import Qa, db
from status_codes import StatusCode

qa_bp = Blueprint('qa_bp', __name__)

@qa_bp.route('/qa', methods=['POST'])
def create_qa():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({"error": "question is required"}), StatusCode.BAD_REQUEST.value

    try:
        print(f"Received question: {data['question']}")
        print(f"Received answer: {data['answer']}")

        new_qa = Qa(data['question'], data['answer'])
        db.session.add(new_qa)
        db.session.commit()
        return jsonify(new_qa.to_dict()), StatusCode.CREATED.value
    except Exception as e:
        db.session.rollback()

        print(f"Error saving to database: {str(e)}")  # Log the specific error

        return jsonify({"error": str(e)}), StatusCode.INTERNAL_SERVER_ERROR.value

@qa_bp.route('/history', methods=['GET'])
def get_history():
    history = Qa.query.all()
    return jsonify([question.to_dict() for question in history]), StatusCode.SUCCESS.value




