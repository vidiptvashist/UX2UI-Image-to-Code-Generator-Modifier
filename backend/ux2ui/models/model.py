from ui2ux.load_variables import *
from google.generativeai import types
from PIL import Image
import io

# 1. Text-only input
def generate_from_text(prompt: str):
    response = model.generate_content(prompt)
    return response.text


# 2. Text + one image
def generate_from_text_and_image(prompt: str, image_path: str):
    with open(image_path, 'rb') as f:
        image_data = f.read()

    image_part = types.Part.from_bytes(data=image_data, mime_type='image/png')

    response = model.generate_content([prompt, image_part])
    return response.text


# 3. Text + two images
def generate_from_text_and_two_images(prompt: str, image_path1: str, image_path2: str):
    with open(image_path1, 'rb') as f1:
        image1_data = f1.read()
    with open(image_path2, 'rb') as f2:
        image2_data = f2.read()

    image_part1 = types.Part.from_bytes(data=image1_data, mime_type='image/png')
    image_part2 = types.Part.from_bytes(data=image2_data, mime_type='image/png')

    response = model.generate_content([prompt, image_part1, image_part2])
    return response.text

