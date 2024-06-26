!pip install ollama

import base64
import requests
import json

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')

# Path to your image
image_path = "/content/EO_176538.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)
basophil_image = encode_image("/content/BA_229935.jpg")
eosinophil_image = encode_image("/content/EO_74387.jpg")
lymphocyte_image = encode_image("/content/LY_164944.jpg")
monocyte_image = encode_image("/content/MO_85774.jpg")
neutrophil_image = encode_image("/content/SNE_746001.jpg")
band_image = encode_image("/content/BNE_53949.jpg")


import ollama
from ollama import Client
client = Client(host='INSERT_YOUR_HOST_HERE')
response = client.chat(model='llava:34b-v1.6',
                       options = {"temperature": 0},
                       messages=[
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{basophil_image}",
      "content": "This image features a basophil.",
      "image": f"data:image/jpeg;base64,{eosinophil_image}",
      "content": "This image features an eosinophil.",
      "image": f"data:image/jpeg;base64,{lymphocyte_image}",
      "content": "This image features a lymphocyte.",
      "image": f"data:image/jpeg;base64,{monocyte_image}",
      "content": "This image features a monocyte.",
      "image": f"data:image/jpeg;base64,{neutrophil_image}",
      "content": "This image features a neutrophil.",
      "image": f"data:image/jpeg;base64,{band_image}",
      "content": "This image features a band neutrophil.",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{base64_image}"
    }
])

print(response['message']['content'])
