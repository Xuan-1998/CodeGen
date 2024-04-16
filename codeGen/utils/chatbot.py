import openai
import re
import os

ENDPOINT = "https://azure-openai-api.shenmishajing.workers.dev/v1"

def parse_response(response) -> tuple[str, str]:
    code = re.findall("```\w*[^`]+```*", response.choices[0].message.content)[
        -1
    ]
    code = "\n".join(code.split("\n")[1:-1])
    return code, response.choices[0].message.content

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
