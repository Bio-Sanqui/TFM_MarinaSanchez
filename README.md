# TFM_MarinaSanchez
This repository was created to contain the code used in the master's thesis titled "Exploring large vision-language models with prompt engineering for peripheral blood cell image analysis and classification" by Marina Sánchez.

In the "GPT-4 Prompts" folder, you will find the code and prompts used to test the capabilities of **GPT-4** for peripheral blood cell image analysis and classification. These can be used by inserting your OpenAI key in the "api_key" variable. To experiment with other GPT-4 models, replace the "model" variable inside "payload" with "gpt-4-vision-preview" (GPT-4V), "gpt-4-turbo" (GPT-4 Turbo), or "gpt-4o" (GPT-4o). The images used to perform few-shot prompting with these models are available in the "Cell images" folder. 

The Claude3 models Haiku, Sonnet and Opus were tested using Anthropic's Workbench, so we did not write any code. Likewise, we performed Zero-shot with LLaVa (llava-v1.6-34b) using its online interface. Nonetheless, we carried out one-shot and two-shot prompting using an API, employing **Ollama** as a framework to run the model and the Jarvislabs platform to rent a powerful and affordable GPU. This code is found in the "LLaVa Few-shot Prompts" folder and can be used by inserting your host in "client".

The .py and .html files used to create the **web application** with Flask are available as "app.py" and "index.html".
