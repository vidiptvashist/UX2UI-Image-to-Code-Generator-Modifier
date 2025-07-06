import json

def parse_html(html, app_name):
    with open(f"{app_name}.html", "w", encoding="utf-8") as f:
        f.write(html)
    return html

