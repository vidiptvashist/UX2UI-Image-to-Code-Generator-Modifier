import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from ux2ui.models.model import *

def generateHTML(image_path):
    prompt = """
            You are an expert React/Tailwind developer
            You take screenshots of a reference web page from the user, and then build single page apps 
            using React and Tailwind CSS.

            - Make sure the app looks exactly like the screenshot.
            - Pay close attention to background color, text color, font size, font family, 
            padding, margin, border, etc. Match the colors and sizes exactly.
            - Use the exact text from the screenshot.
            - Do not add comments in the code such as "<!-- Add other navigation links as needed -->" and "<!-- ... other news items ... -->" in place of writing the full code. WRITE THE FULL CODE.
            - Repeat elements as needed to match the screenshot. For example, if there are 15 items, the code should have 15 items. DO NOT LEAVE comments like "<!-- Repeat for each news item -->" or bad things will happen.
            - For images, use placeholder images from https://placehold.co and include a detailed description of the image in the alt text so that an image generation AI can generate the image later.

            In terms of libraries,

            - Use these script to include React so that it can run on a standalone page:
                <script src="https://cdn.jsdelivr.net/npm/react@18.0.0/umd/react.development.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/react-dom@18.0.0/umd/react-dom.development.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/@babel/standalone/babel.js"></script>
            - Use this script to include Tailwind: <script src="https://cdn.tailwindcss.com"></script>
            - You can use Google Fonts
            - Font Awesome for icons: <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>

            Return only the full code in <html></html> tags.
            Do not include markdown "```" or "```html" at the start or end.
            """
    response = generate_from_text_and_image(prompt, image_path)
    return response

def explanationHTML(html_code):
    prompt = f"""
    Project HTML Code Explanation
    Please explain the HTML code I'm sharing as if you're helping someone understand what this project does and how it works. Focus on:

    Project Overview: What is this website/application trying to accomplish? What problem does it solve or what purpose does it serve?
    User Experience: What will users see and be able to do when they visit this page? Walk through the user journey.
    Main Features: What are the key functionalities and components that make this project work?
    Content & Layout: How is the information organized and presented to users?
    Interactive Elements: What can users click, fill out, or interact with? How do these interactions work?
    Technical Implementation: Briefly explain the technical approach without getting too deep into code details.
    Project Goals: Based on the structure and content, what appears to be the main objectives of this project?

    Please explain this in plain language that a non-technical person could understand, focusing on the "what" and "why" rather than technical implementation details.
    HTML Code to Explain: 
        {html_code}
            """
    response = generate_from_text(prompt)
    return response





