import openai
import re
import os
import requests
import json
from .codeGen_logger import *

ENDPOINT = "https://azure-openai-api.shenmishajing.workers.dev/v1"
logger = setup_logging()


def parse_code_block(response) -> str:
    code_block = re.search('```(.*?)```', response, re.DOTALL)
    if code_block:
        return code_block.group(1)
    return response


def string_to_list(string):
    string = string.strip()
    if not string:
        return []
    pattern = r'"(.*?)"'
    string_list = re.findall(pattern, string)
    return string_list


class ChatbotAPI:
    def __init__(self, model: str) -> None:
        self.model = model

    def create(self, messages: list[dict]) -> str:
        raise NotImplementedError


class ChatCompletionAPI(ChatbotAPI):
    def __init__(self, model="gpt-3.5-turbo") -> None:
        super().__init__(model)
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=ENDPOINT)
        self.chatbot = client.chat.completions

    def create(self, messages: list[dict], n=1, temperature=0.5) -> str:
        response = self.chatbot.create(
                model=self.model, messages=messages, temperature=temperature, n=n
            ).choices[0].message.content
        logger.debug(f"ChatCompletionAPI response: {response}")
        return parse_code_block(response), response


class AzureOpenaiChatCompletionAPI(ChatbotAPI):
    def __init__(self, model="gpt-4") -> None:
        super().__init__(model)
        client = openai.AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-02-01",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )
        self.chatbot = client.chat.completions

    def create(self, messages: list[dict], n=1, temperature=0.5) -> str:
        response = self.chatbot.create(
            model=self.model, messages=messages, temperature=temperature, n=n
        ).choices[0].message.content
        logger.debug(f"AzureOpenaiChatCompletionAPI response: {response}")
        return parse_code_block(response), response


class OllamaAPI(ChatbotAPI):
    def __init__(self, model="llama3") -> None:
        super().__init__(model)

    def create(self, messages: list[dict]) -> str:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": self.model, "messages": messages, "stream": False},
        )
        response_content = json.loads(response.content)["message"]["content"]
        logger.debug(f"OllamaAPI response: {response_content}")
        return parse_code_block(response_content), response_content

    def generate(self, prompt: str) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False},
        )
        return json.loads(response.content)["message"]["content"]
