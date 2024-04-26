import openai
import re
import os
import requests
import json

ENDPOINT = "https://azure-openai-api.shenmishajing.workers.dev/v1"

def parse_code_block(response) -> str:
    code = re.findall("```\w*[^`]+```*", response)[
        -1
    ]
    return "\n".join(code.split("\n")[1:-1])

def parse_response(response) -> tuple[str, str]:
    code = parse_code_block(response.choices[0].message.content)
    return code, response.choices[0].message.content

def string_to_list(string):
    string = string.strip()
    if not string:
        return []
    pattern =  r'"(.*?)"'
    string_list = re.findall(pattern, string)
    return string_list

def parse_response_py_list(response) -> tuple[list[str], str]:
    code, response = parse_response(response)
    return string_to_list(code), response

class ChatCompletionAPI:
    def __init__(self, model="gpt-3.5-turbo") -> None:
        client = openai.OpenAI(
            api_key=os.environ.get("OPENAI_KEY"),
            base_url=ENDPOINT
        )
        self.model = model
        self.chatbot = client.chat.completions

    def create(self, messages: list[dict], n=1, temperature=0.5) -> str:
        return self.chatbot.create(
            model=self.model, messages=messages, temperature=temperature, n=n
        )


class EmbeddingAPI:
    def __init__(self, model="text-embedding-ada-002") -> None:
        client = openai.OpenAI(
            api_key=os.environ.get("OPENAI_KEY"),
            base_url=ENDPOINT
        )
        self.model = model
        self.embedding = client.embeddings

    def create(self, text) -> list[float]:
        return self.embedding.create(model=self.model, input=text)

class OllamaAPI:
    def __init__(self, model="llama3") -> None:
        self.model = model

    def chat(self, messages) -> str:
        response = requests.post('http://localhost:11434/api/chat', json={
        'model': self.model,
        'messages': messages,
        'stream': False
        })
        return json.loads(response.content)['message']['content']
    
    def generate(self, prompt: str) -> str:
        response = requests.post('http://localhost:11434/api/generate', json={
            'model': self.model,
            'prompt': prompt,
            'stream': False
        })
        return json.loads(response.content)['message']['content']
