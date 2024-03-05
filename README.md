# vertexai-prompt-to-text
# Text Generation API for Prompt-to-Text using Google Vertex AI

## Set Up a Google Cloud Project
- If you haven't already, create a Google Cloud project in the Google Cloud Console.

## Enable Vertex AI API
- Navigate to the "Products and Solutions" > "Artificial Intelligence" page in the Google Cloud Console.
- Search for "Vertex AI API" and enable it for your project.

## Set Up Authentication
- Install the Google Cloud SDK (gcloud) CLI tool.
- You can use service account credentials or create new ones. [Here's a guide](https://developers.google.com/workspace/guides/create-credentials#gcloud-cli).
- Place the JSON file containing your service account credentials under the `config/` folder in your project.
- Rename the JSON file to `service-account-key.json`.

## Install Necessary Libraries
- Install Python and necessary Python libraries for working with Google Cloud services and PALM2 text generation.
- Include libraries such as `vertexai`, `flask` and `google-auth`.

## Write and Run the Script
- Write a Python script (`server.py` for example) for serving the text generation model.
- Run this command from your project: `python server.py`.

## Make API Call
- Use an HTTP client like Postman to make API calls and get responses.
- Endpoint URL: `<hostname>/api/data`.
- Parameters: `{ "prompt": "<prompt text>" }`.

## References
- [Vertex AI Quickstart for Generative AI](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-text#generative-ai-test-text-prompt-python_vertex_ai_sdk)
- [Vertex AI Generative AI Model Reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text#request_body)
