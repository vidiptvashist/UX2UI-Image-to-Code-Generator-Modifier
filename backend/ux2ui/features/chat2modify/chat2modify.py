import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from ux2ui.models.model import *

def read_html(app_name):
    with open(f"{app_name}.html", 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

def modifyHTML(query,app_name):
    html_code = read_html(app_name)
    prompt = f"""
    # HTML Modification Prompt

    You are an expert HTML/CSS/Tailwind developer who specializes in modifying existing HTML code based on user requests.

    You will receive:
    1. Existing HTML code
    2. User query describing what changes they want

    Your task:
    - Analyze the user's modification request carefully
    - Make the requested changes to the existing HTML code
    - Preserve all existing functionality and structure unless specifically asked to change it
    - Use appropriate Tailwind CSS classes for styling modifications
    - Maintain the same libraries and dependencies (React, Tailwind, Font Awesome, etc.)
    - Keep the same responsive design patterns
    - For color changes, use appropriate Tailwind color classes
    - For layout changes, modify the relevant Tailwind utility classes
    - For content changes, update the actual text/content as requested
    - For component changes, add/remove/modify the HTML elements as needed

    Guidelines:
    - Pay attention to the user's exact wording - if they say "change background to black", change background colors
    - If they say "make text white", change text colors
    - If they say "make it larger", increase font sizes or element sizes
    - If they say "center it", add appropriate centering classes
    - If they say "add padding", increase padding classes
    - If they say "remove border", remove border classes
    - Be smart about related changes - if background becomes dark, consider if text needs to be lighter
    - Preserve all placeholder images and their alt text descriptions
    - Keep all existing JavaScript functionality intact
    - Maintain all existing class structures and only modify what's specifically requested

    Return only the full modified HTML code in <html></html> tags.
    Do not include markdown "```" or "```html" at the start or end.
    Do not add any explanatory text or comments about the changes made.

    INPUT HTML CODE: {html_code}
    USER QUERY: {query}
            """
    response = generate_from_text(prompt)
    return response

def explanationHTML_changes(original_html,modified_html, query ):
    prompt = f"""
    You are an expert HTML/CSS/Tailwind code analyzer who specializes in identifying and explaining changes between two versions of HTML code.

    You will receive:
    1. Old HTML code (original version)
    2. New HTML code (modified version)
    3. User query that was used to make the modifications

    Your task:
    - Compare the old HTML code with the new HTML code
    - Identify all the specific changes that were made
    - Explain what exactly got changed in response to the user query
    - Provide a clear, detailed analysis of the modifications

    Focus on identifying changes in:
    - CSS classes (especially Tailwind classes)
    - Background colors, text colors, font sizes
    - Layout properties (padding, margin, positioning)
    - Element structure (added/removed elements)
    - Content changes (text modifications)
    - Style attributes
    - Class additions/removals/modifications

    Format your response as follows:

    ## Changes Made Based on User Query: "[user query]"

    ### 1. [Change Category] Changes:
    - **Before**: [what it was]
    - **After**: [what it became]
    - **Impact**: [what this change accomplishes]

    ### 2. [Change Category] Changes:
    - **Before**: [what it was]
    - **After**: [what it became]
    - **Impact**: [what this change accomplishes]

    [Continue for all identified changes...]

    ### Summary:
    [Brief summary of all changes and how they fulfill the user's request]

    Be specific about:
    - Exact class names that changed
    - Color values that changed
    - Size modifications
    - Layout adjustments
    - Any structural changes
    - Content modifications

    If no changes were detected, state "No changes detected between the old and new HTML code."

    INPUT:
    
    1. Old HTML code: {original_html}
    2. New HTML code {modified_html}
    3. User query: {query}
    """
    response = generate_from_text(prompt)
    return response
