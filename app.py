from flask import Flask, render_template, request
import base64
import requests

app = Flask(__name__)
api_key = "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"

def gpt4(base64_image):
    # Function to encode images
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    # Getting the base64 string
    basophil_image1 = encode_image("BA_229935.jpg")
    basophil_image2 = encode_image("BA_594501.jpg")
    eosinophil_image1 = encode_image("EO_74387.jpg")
    eosinophil_image2 = encode_image("EO_280451.jpg")
    lymphocyte_image1 = encode_image("LY_164944.jpg")
    lymphocyte_image2 = encode_image("LY_320312.jpg")
    monocyte_image1 = encode_image("MO_85774.jpg")
    monocyte_image2 = encode_image("MO_116840.jpg")
    neutrophil_image = encode_image("SNE_746001.jpg")
    band_image = encode_image("BNE_53949.jpg")
    # Generate openai response
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the blood cell type in these images:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{basophil_image1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{basophil_image2}"
                        }
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "These images feature a basophil."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the blood cell type in these images:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{eosinophil_image1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{eosinophil_image2}"
                        }
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "These images feature an eosinophil."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the blood cell type in these images:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{lymphocyte_image1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{lymphocyte_image2}"
                        }
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "These images feature a lymphocyte."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the blood cell type in these images:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{monocyte_image1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{monocyte_image2}"
                        }
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "These images feature a monocyte."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the blood cell type in these images:"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{neutrophil_image}"
                        }
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
                        "text": "These images feature a neutrophil."
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
    text_response = response.json()
    content_response = text_response['choices'][0]['message']['content']
    return content_response

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def get_image():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = "static/" + img.filename
        img.save(img_path)
        with open(img_path, "rb") as image_file:
            image64 = base64.b64encode(image_file.read()).decode('utf-8')
        cell_type = gpt4(image64)
    return render_template("index.html", response=cell_type, img_path=img_path)


if __name__ == '__main__':
    app.run(debug=True)