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
          "text": "This image features a basophil."
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
          "text": "This image features an eosinophil."
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
          "text": "This image features a lymphocyte."
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
          "text": "This image features a monocyte."
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
          "text": "This image features a neutrophil."
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
          "text": "This image features a band neutrophil."
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
