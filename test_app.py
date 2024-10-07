import pytest
from flask import Flask
from unittest.mock import MagicMock

# Assuming your Flask app is called 'app' and you import it here
from app import app

@pytest.fixture
def client():
    """Flask test client for making requests to your app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ask_question(client, mocker):
    """Test the /ask route by mocking the OpenAI API."""

    # Mock the OpenAI API call
    mock_openai = mocker.patch('openai.chat.completions.create')
    print("Mock applied: ", mock_openai)

    # Set the mock response
    mock_openai.return_value = {
        "choices": [
            {
                "message": {
                    "content": "This is a mocked response."
                }
            }
        ]
    }

    # Send a POST request to the /ask route
    response = client.post('/ask', json={
        "question": "What is the capital of France?"
    })

    # Parse the JSON response
    data = response.get_json()

    # Assertions
    assert response.status_code == 200
    assert data['question'] == "What is the capital of France?"
    assert data['answer'] == "This is a mocked response."

    # Ensure the OpenAI API was called with the correct parameters
    mock_openai.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ],
        max_tokens=100
    )
