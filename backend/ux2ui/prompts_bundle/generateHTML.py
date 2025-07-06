from ui2ux.models.model import *

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

image_path = r"C:\Users\Vidipt\Desktop\project\ui2ux\sample_ux\sample00.png"
generateHTML(image_path)