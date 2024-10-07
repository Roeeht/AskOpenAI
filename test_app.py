import pytest
from flask import Flask
import openai
import json
from app import app  # Assuming your Flask app is in app.py

# Mock OpenAI API response
@pytest.fixture
def mock_openai(monkeypatch):
    class MockCompletion:
        @staticmethod
        def create(engine, prompt, max_tokens):
            return {
                'choices': [{
                    'text': 'This is a mock response.'
                }]
            }

    monkeypatch.setattr(openai.resources.Completions, 'create', MockCompletion.create)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_ask_endpoint(client, mock_openai):
    # Define the payload to send to the /ask endpoint
    payload = {
        "question": "What is the capital of France?"
    }

    # Make the POST request to the /ask endpoint
    response = client.post('/ask', 
                           data=json.dumps(payload),
                           content_type='application/json')

    # Parse the response JSON
    data = response.get_json()

    # Assertions
    assert response.status_code == 200
    assert 'question' in data
    assert 'answer' in data
    assert data['question'] == "What is the capital of France?"
    assert data['answer'] == "This is a mock response."
