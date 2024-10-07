from urllib import request
from flask import Blueprint

general_bp = Blueprint('general_bp', __name__)

@general_bp.route('/')
def home():
    return "Hello, Flask!"

@general_bp.route('/about')
def about():
    return "This is the about page."

@general_bp.route('/ask', methods=['POST'])
def ask_question():
    # Get the question from the JSON payload
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Call the OpenAI API to get the answer
        response = openai.Completion.create(
            engine="text-davinci-003",  # or any other model like 'gpt-3.5-turbo'
            prompt=question,
            max_tokens=100
        )
        
        # Extract the response text from OpenAI
        answer = response['choices'][0]['text'].strip()

        # Return the question and answer as a JSON response
        return jsonify({"question": question, "answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
