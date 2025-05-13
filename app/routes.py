from flask import Blueprint, jsonify, request
from google import genai
import json

rec = Blueprint('main', __name__, url_prefix='/recommend')
api_key = "AIzaSyA-fYrGkcE6om7Jj96NHax9Zd4OYpLPMaQ"

@rec.route('/', methods=['POST'])
def index():
    # Get the custom text string from the request JSON payload
    data = request.get_json()  # Parse JSON payload from the frontend
    print(data)
    # Extract the 'requirement' field, default to empty string if not provided
    requirement = data.get('requirement')
    # Form the query string to GPT models
    query_str = f"For this requirement description of a research survey: \"{requirement}\", help me generate an one-hot encoding feature to represent the requirement text and generate one ideal vector that would fit the requirement perfectly, using only features that express the affirmative eligibility criteria (do not include complementary or negative features). Finalize the response in a json format where there're 2 fields, \"vector\" field represent the one-hot-encoding vector, and \"features\" field represents an array of the features's meaning"
    query_str = f"Given this requirement: \"{requirement}\", generate a one-hot encoding feature vector for the requirement only, using only features that express the affirmative eligibility criteria (do not include complementary or negative features). An ideal candidate should answer \"yes\" to all the feature question. Finalize the response in a json format where there's 1 field \"features\" representing an array of the features's meaning"
    query_str = f"Given this requirement: \"{requirement}\", generate a list of short yes/no questions to determine a candidate's eligibility, using only questions that express the affirmative eligibility criteria (do not include complementary or negative questions). Form the questions so that an ideal candidate should answer \"yes\" to all of them. Finalize the response in a json format where there's 1 field \"questions\" representing an array of the questions"
    # Input to GPT model
    response = embedding(query_str)
    print(response)
    return jsonify(response["questions"])  # Return JSON response

client = genai.Client(api_key=api_key)

def embedding(requirement):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=requirement
    )
    responses = extract_json(response.text)
    return responses
    

def extract_json(response_text):
    # Extract the portion of the string between the first '{' and the last '}'
    start = response_text.find('{')
    end = response_text.rfind('}') + 1
    json_str = response_text[start:end]
    
    # Convert the extracted string to a JSON object
    try:
        json_data = json.loads(json_str)
        return json_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None