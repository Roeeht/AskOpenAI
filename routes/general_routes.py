import traceback
from flask import Blueprint, request, jsonify
import openai
from config import Config

# Create the blueprint
general_bp = Blueprint('general_bp', __name__)

# Set OpenAI API key from the environment variables via Config
openai.api_key = Config.OPENAI_API_KEY

@general_bp.route('/ask', methods=['POST'])
def ask_question():
    # Get the question from the JSON payload
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Call the OpenAI API to get the answer
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=100
        )
        
        # Extract the response text from OpenAI
        answer = response['choices'][0]['message']['content'].strip()

        # Return the question and answer as a JSON response
        return jsonify({"question": question, "answer": answer})


    except Exception as e:
        # Print full traceback for any other errors
        print(f"Unexpected error: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
