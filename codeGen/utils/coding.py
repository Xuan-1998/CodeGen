from .chatbot import *
from .problems import *
from .prompts import *
from tqdm import tqdm
from typing import Callable
from tenacity import retry, stop_after_attempt, retry_if_result, retry_if_exception_type

RETRY_COUNT = 15


class Coding:
    def __init__(
        self,
        statement: str,
        chatbot: ChatbotAPI,
        retry_count: int = RETRY_COUNT,
    ) -> None:
        self.statement = statement
        self.chatbot = chatbot
        self.retry_count = retry_count

    @retry( stop=stop_after_attempt(RETRY_COUNT), retry=( retry_if_result(lambda result: len(result[0]) == 0) | retry_if_exception_type(IndexError) ))
    def transformation_coder(self, transformation: str) -> tuple[str, str]:
        messages = [
            {
                "role": "system",
                "content": CODING_SYSTEM.format(statement=self.statement),
            },
            {
                "role": "user",
                "content": CODING_TRANSFORMATION.format(transformation=transformation),
            },
        ]

        return self.chatbot.create(messages)

    def zeroshot_coder(self) -> tuple[str, str]:
        message = [
            {
                "role": "system",
                "content": CODING_SYSTEM.format(statement=self.statement),
            },
            {"role": "user", "content": CODING_ZEROSHOT},
        ]

        return self.chatbot.create(message)

    def algorithm_coder(self, algorithm: str) -> tuple[str, str]:
        messages = [
            {
                "role": "system",
                "content": CODING_SYSTEM.format(statement=self.statement),
            },
            {
                "role": "user",
                "content": CODING_ALGORITHM.format(algorithm=algorithm),
            },
        ]
        return self.chatbot.create(messages)

    def transformation_algorithm_coder(
        self, algorithm: str, transformation: str
    ) -> tuple[str, str]:
        code, response = self.chatbot.create(
            [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=self.statement),
                },
                {
                    "role": "user",
                    "content": CODING_TRANSFORMATION_ALGORITHM.format(
                        statement=self.statement,
                        algorithm=algorithm,
                        transformation=transformation,
                    ),
                },
            ]
        )
        return code, response

    def provide_algorithm_coder(self, algorithm: str) -> tuple[str, str]:
        messages = [
            {
                "role": "system",
                "content": CODING_SYSTEM.format(statement=self.statement),
            },
            {
                "role": "user",
                "content": PROVIDE_ALGORITHM.format(
                    statement=self.statement, algorithm=algorithm
                ),
            },
        ]
        raw_list, response = self.chatbot.create(messages)
        result_list = string_to_list(raw_list)
        return result_list, response

    @retry( stop=stop_after_attempt(RETRY_COUNT), retry=( retry_if_result(lambda result: len(result[0]) == 0) | retry_if_exception_type(IndexError) ), )
    def provide_algorithm_coder2(self, algorithm: str) -> tuple[str, str]:
        messages = [
            {
                "role": "system",
                "content": ALGORITHM_SYSTEM,
            },
            {
                "role": "user",
                "content": algorithm,
            },
        ]
        raw_list, response = self.chatbot.create(messages)
        result_list = string_to_list(raw_list)
        return result_list, response

    @retry(
        stop=stop_after_attempt(RETRY_COUNT),
        retry=(
            retry_if_result(lambda result: len(result[0]) == 0)
            | retry_if_exception_type(IndexError)
        ),
    )
    def follow_up_coder(
        self, algorithm: str, step: str, steps: list[str]
    ) -> tuple[str, str]:
        messages = [
            {
                "role": "system",
                "content": CODING_SYSTEM.format(statement=self.statement),
            },
            {
                "role": "user",
                "content": FOLLOW_UP_ALGORITHM.format(
                    statement=self.statement,
                    algorithm=algorithm,
                    step=step,
                    steps="\n".join(steps),
                ),
            },
        ]

        raw_list, response = self.chatbot.create(messages)
        result_list = string_to_list(raw_list)
        return result_list, response

    @retry( stop=stop_after_attempt(RETRY_COUNT), retry=( retry_if_result(lambda result: len(result[0]) == 0) | retry_if_exception_type(IndexError) ), )
    def evaluation_coder(self, algorithm: str, transformation: str) -> tuple[str, str]:
        messages = [
            {
                "role": "system",
                "content": CODING_SYSTEM.format(statement=self.statement),
            },
            {
                "role": "user",
                "content": TRANSFORMATION_EVALUATION.format(
                    algorithm=algorithm, transformation=transformation
                ),
            },
        ]
        return self.chatbot.create(messages)
