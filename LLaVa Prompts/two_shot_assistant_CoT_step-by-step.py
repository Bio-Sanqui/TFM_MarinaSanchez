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
image_path = "/content/BNE_752441.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)
basophil_image1 = encode_image("/content/BA_229935.jpg")
basophil_image2 = encode_image("/content/BA_594501.jpg")
eosinophil_image1 = encode_image("/content/EO_74387.jpg")
eosinophil_image2 = encode_image("/content/EO_280451.jpg")
lymphocyte_image1 = encode_image("/content/LY_164944.jpg")
lymphocyte_image2 = encode_image("/content/LY_320312.jpg")
monocyte_image1 = encode_image("/content/MO_85774.jpg")
monocyte_image2 = encode_image("/content/MO_116840.jpg")
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
      "image": f"data:image/jpeg;base64,{basophil_image1}"
    },
    {
      "role": "assistant",
      "content": "This image features a basophil. Basophils stand out with their intermediate size, low nucleocytoplasmic ratio, and a segmented nucleus whose segments can vary. They contain dark, condensed/heterogeneous nuclear chromatin and a wide azurophilic cytoplasm with round basophilic granulation. The large number of dark purplish granules often make the nucleus difficult to see."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{basophil_image2}"
    },
    {
      "role": "assistant",
      "content": "This image features a basophil. Basophils stand out with their intermediate size, low nucleocytoplasmic ratio, and a segmented nucleus whose segments can vary. They contain dark, condensed/heterogeneous nuclear chromatin and a wide azurophilic cytoplasm with round basophilic granulation. The large number of dark purplish granules often make the nucleus difficult to see."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{eosinophil_image1}"
    },
    {
      "role": "assistant",
      "content": "This image features an eosinophil. Eosinophils, with an intermediate size and low nucleocytoplasmic ratio, are recognized by their distinctly segmented nucleus, with 2 segments, and condensed/heterogeneous nuclear chromatin. Their wide cytoplasm is eosinophilic, complemented by round dark-pink granules."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{eosinophil_image2}"
    },
    {
      "role": "assistant",
      "content": "This image features an eosinophil. Eosinophils, with an intermediate size and low nucleocytoplasmic ratio, are recognized by their distinctly segmented nucleus, with 2 segments, and condensed/heterogeneous nuclear chromatin. Their wide cytoplasm is eosinophilic, complemented by round dark-pink granules."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{lymphocyte_image1}"
    },
    {
      "role": "assistant",
      "content": "This image features a lymphocyte. Lymphocytes are small but have a high nucleocytoplasmic ratio. Their nucleus is round and mononuclear, with condensed/heterogeneous chromatin without nucleoli. Their scant, basophilic cytoplasm shows only occasional granulation."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{lymphocyte_image2}"
    },
    {
      "role": "assistant",
      "content": "This image features a lymphocyte. Lymphocytes are small but have a high nucleocytoplasmic ratio. Their nucleus is round and mononuclear, with condensed/heterogeneous chromatin without nucleoli. Their scant, basophilic cytoplasm shows only occasional granulation."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{monocyte_image1}"
    },
    {
      "role": "assistant",
      "content": "This image features a monocyte. Monocytes are characterized by their high size and moderate nucleocytoplasmic ratio. They exhibit an indented nucleus described as mononuclear, with low condensed nuclear chromatin. The cytoplasm of a monocyte is moderate in volume, displaying a grayish colour that accompanies its fine sand-like granulation."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{monocyte_image2}"
    },
    {
      "role": "assistant",
      "content": "This image features a monocyte. Monocytes are characterized by their high size and moderate nucleocytoplasmic ratio. They exhibit an indented nucleus described as mononuclear, with low condensed nuclear chromatin. The cytoplasm of a monocyte is moderate in volume, displaying a grayish colour that accompanies its fine sand-like granulation."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{neutrophil_image}"
    },
    {
      "role": "assistant",
      "content": "This image features a neutrophil. Neutrophils are intermediate-sized blood cells characterized by a low nucleocytoplasmic ratio. Its nucleus is segmented into 2 to 5 parts and features condensed/heterogeneous chromatin with no nucleoli present. The cytoplasm is wide and azurophilic, containing azurophil granulation."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image:",
      "image": f"data:image/jpeg;base64,{band_image}"
    },
    {
      "role": "assistant",
      "content": "This image features a neutrophil. Neutrophils are intermediate-sized blood cells characterized by a low nucleocytoplasmic ratio. Its nucleus is segmented into 2 to 5 parts and features condensed/heterogeneous chromatin with no nucleoli present. The cytoplasm is wide and azurophilic, containing azurophil granulation."
    },
    {
      "role": "user",
      "content": "Identify the blood cell type in this image. Provide a step-by-step reasoning before providing your answer:",
      "image": f"data:image/jpeg;base64,{base64_image}"
    }
])

print(response['message']['content'])
