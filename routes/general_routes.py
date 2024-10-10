import traceback
from flask import Blueprint, request, jsonify
import openai
from config import Config
from status_codes import StatusCode

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
        return jsonify({"error": "No question provided"}), StatusCode.BAD_REQUEST.value

    try:
        # Call the OpenAI API to get the answer
        answer = askOpenAI(question)
        status_code, db_response = updateDB_via_route(question, answer)
       
        if status_code != StatusCode.CREATED.value:
            return jsonify({"error": "Failed to store question and answer in the database"}), StatusCode.INTERNAL_SERVER_ERROR.value
       
        return jsonify({"question": question, "answer": answer}), StatusCode.SUCCESS.value

    except Exception as e:
        # Print full traceback for any other errors
        print(f"Unexpected error: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), StatusCode.INTERNAL_SERVER_ERROR.value


def askOpenAI(question):
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=100
        )
        
        # Extract the response text from OpenAI
    answer = response.choices[0].message.content.strip()
    return answer


def updateDB_via_route(question, answer):
    from app import app

    with app.app_context():
        with app.test_client() as client:
            # Send the data to the existing /qa route
            response = client.post('/qa', json={"question": question, "answer": answer})

            print(f"Request to /qa with question: {question} and answer: {answer}")
            print(f"Status code from /qa: {response.status_code}")
            print(f"Response from /qa: {response.get_json()}")


            return response.status_code, response.get_json()
