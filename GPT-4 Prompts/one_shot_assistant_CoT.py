import base64
import requests

# OpenAI API Key
api_key = "INSERT_YOUR_OPENAI_KEY_HERE"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/content/SNE_968729.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)
basophil_image = encode_image("/content/BA_229935.jpg")
eosinophil_image = encode_image("/content/EO_74387.jpg")
lymphocyte_image = encode_image("/content/LY_164944.jpg")
monocyte_image = encode_image("/content/MO_85774.jpg")
neutrophil_image = encode_image("/content/SNE_746001.jpg")
band_image = encode_image("/content/BNE_53949.jpg")

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{basophil_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image features a basophil.Basophils have an intermediate size, low nucleocytoplasmic ratio, and a segmented nucleus whose segments can vary. They contain dark, condensed/heterogeneous nuclear chromatin and a wide azurophilic cytoplasm with round basophilic granulation. The large number of dark purplish granules often make the nucleus difficult to see."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{eosinophil_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image features an eosinophil.Eosinophils, with an intermediate size and low nucleocytoplasmic ratio, are recognized by their distinctly segmented nucleus, with 2 segments, and condensed/heterogeneous nuclear chromatin. Their wide cytoplasm is eosinophilic, complemented by round dark-pink granules."
        }
      ]
    },
        {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{lymphocyte_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image features a lymphocyte. Lymphocytes are small but have a high nucleocytoplasmic ratio. Their nucleus is round and mononuclear, with condensed/heterogeneous chromatin without nucleoli. Their scant, basophilic cytoplasm shows only occasional granulation."
        }
      ]
    },
        {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{monocyte_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image features a monocyte. Monocytes are characterized by their high size and moderate nucleocytoplasmic ratio. They exhibit an indented nucleus described as mononuclear, with low condensed nuclear chromatin. The cytoplasm of a monocyte is moderate in volume, displaying a grayish colour that accompanies its fine sand-like granulation."
        }
      ]
    },
        {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{neutrophil_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image features a neutrophil. Neutrophils are intermediate-sized blood cells characterized by a low nucleocytoplasmic ratio. Its nucleus is segmented into 2 to 5 parts and features condensed/heterogeneous chromatin with no nucleoli present. The cytoplasm is wide and azurophilic, containing azurophil granulation."
        }
      ]
    },
        {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{band_image}"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "This image features a band neutrophil, a less mature form of a neutrophil. This form has an intermediate size and low nucleocytoplasmic ratio, but its nucleus takes a distinct band shape with no segments. Featuring similar nuclear chromatin and absence of nucleoli, its azurophilic cytoplasm also houses azurophil granulation."
        }
      ]
    },
          {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Identify the blood cell type in this image:"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    },
  ],
  "max_tokens": 4000,
  "temperature": 0,
  "top_p": 0
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
