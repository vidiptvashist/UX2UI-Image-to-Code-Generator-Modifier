import os
import json
import google.generativeai as genai


from dotenv import load_dotenv
import os

load_dotenv()  # load from .env file
api_key = os.getenv("MODEL_API_KEY")


with open(r'ux2ui\params.json') as f:
    config_data = json.load(f)

# api_key = os.environ.get("MODEL_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")