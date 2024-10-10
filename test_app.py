import pytest
from flask import Flask
from unittest.mock import MagicMock
from status_codes import StatusCode
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

    # Set the mock response, matching the structure of the actual API response
    mock_openai.return_value = MagicMock(choices=[MagicMock(message=MagicMock(content="This is a mocked response."))])

    # Send a POST request to the /ask route
    response = client.post('/ask', json={
        "question": "What is the capital of France?"
    })

        # Print response for debugging
    print(f"Response status code: {response.status_code}")
    print(f"Response data: {response.get_json()}")


    # Parse the JSON response
    data = response.get_json()

    # Assertions
    assert response.status_code == StatusCode.SUCCESS.value
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


