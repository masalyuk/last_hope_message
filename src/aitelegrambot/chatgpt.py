import openai

# Set your OpenAI API key

import base64
import requests
from constants import *
# OpenAI API Key
#openai.api_key = "OPENAI_TOKEN"

from openai import OpenAI

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

###
def generate_promt_cringe(img_path):
        str = PROMT_BASE.substitute()
        dscr = describe_profile(img_path, " ")
        query = str + " Description Tinder Profile: " + dscr
        print("==========")
        print(query)
        print("==========")
        return query

def describe_profile(image_path, text):
    base64_image = encode_image(image_path)

    client = OpenAI(api_key=openai.api_key)

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text", 
            "text": "Describe this tinder profile"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
            },
            }],
        }
    ],
    max_tokens=3000,
    )

    return str(response.choices[0].message.content)
