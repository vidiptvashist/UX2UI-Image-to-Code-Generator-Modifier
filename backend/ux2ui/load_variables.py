import os
import json
import google.generativeai as genai

with open('ui2ux/params.json') as f:
    config_data = json.load(f)

api_key = os.environ.get("MODEL_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
