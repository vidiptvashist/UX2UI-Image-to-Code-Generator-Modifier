import json

def parse_html(html, app_name):
    with open(f"{app_name}.html", "w", encoding="utf-8") as f:
        f.write(html)
    return html


def process_react(response):
    response = response.replace("```json", "").replace("```", "").strip()
    return json.loads(response)


import os

def save_files(folder_name, file_dict):
    os.makedirs(folder_name, exist_ok=True)

    for file_name, code in file_dict.items():
        file_name = file_name.strip()

        file_path = os.path.join(folder_name, file_name)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        print(f"Saved: {file_path}")