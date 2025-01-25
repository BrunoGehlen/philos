from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from dotenv import load_dotenv

from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes



# Initialize a free LLM (you can use OpenAI's model or any other LLM supported by LangChain)
# Make sure you have the required API key configured if using OpenAI
llm = OpenAI(model_name="text-davinci-003", temperature=0.7)

@app.route('/', methods=['POST'])
def process_content():
    try:
        # Parse the incoming JSON body
        data = request.get_json()
        print(data)
        if not data or 'content' not in data:
            return jsonify({"error": "Invalid request. 'content' parameter is required."}), 400

        # Get the content from the request body
        content = data['content']

        # Use the LLM to process the content
        response = llm(content)

        # Return the response from the LLM
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)