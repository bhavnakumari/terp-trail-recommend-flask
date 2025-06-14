# My Flask App

Integration with External Services Google Gemini API: We built functionality in our posting creation service that sends posting descriptions to the Google Gemini API. The API converts these into a set of screening questions which are then used to dynamically gather volunteer responses and compute a score. Flask-Based Recommendation Engine: Our recommendation system, built in Flask, processes past application data and volunteer profiles. This service provides insights and personalized suggestions to research firms, enhancing candidate matching and streamlining the recruitment process.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
├── requirements.txt
└── README.md
```

## Requirements

To run this application, you need to have Python and Flask installed. You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:
   ```
   cd my-flask-app
   ```

2. Set the `FLASK_APP` environment variable:
   - On macOS/Linux:
     ```
     export FLASK_APP=app
     ```
   - On Windows:
     ```
     set FLASK_APP=app
     ```

3. Run the application:
   ```
   flask run
   ```

4. Open your web browser and go to `http://127.0.0.1:5000/` to see the "Hello, World!" message.
