from flask import Flask, jsonify, request
import vertexai
from vertexai.language_models import TextGenerationModel
import os
from google.auth import default

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/service-account-key.json"


app = Flask(__name__)
credentials, project_id = default()


def generateText(
    project_id: str,
    location: str,
) -> str:

    vertexai.init(project=project_id, location=location)

    # Get query parameters from the request
    request_data = request.get_json()
    if not request_data or 'prompt' not in request_data:
        return jsonify({'error': 'Invalid JSON data or missing "prompt" key'}), 400


    # override these parameters as needed:
    parameters = {
        "temperature": 0.0,  # Temperature controls the degree of randomness in token selection -  0.0–1.0
        "max_output_tokens": 50,  # Token limit determines the maximum amount of text output. - 1–1024
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value. - 0.0–1.0
        "top_k": 1,  # A top_k of 1 means the selected token is the most probable among all tokens. - 1–40
    }

    prompt = str(request_data.get('prompt'))
    model = TextGenerationModel.from_pretrained("text-bison@002")
    response = model.predict(
        prompt,
        **parameters,
    )
    #print(f"Response from Model: {response.text}")

    return response.text
    
@app.route('/api/data', methods=['POST'])
def getData():
    data = generateText('prompt-to-text-ai-project', 'us-central1')
    return data

if __name__ == '__main__':
    app.run(debug=True)


