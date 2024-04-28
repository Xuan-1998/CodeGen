from .chatbot import ChatCompletionAPI, parse_response, parse_response_py_list, OllamaAPI, parse_code_block, string_to_list
from .problems import *
from tqdm import tqdm
from typing import Callable
from tenacity import retry, stop_after_attempt, retry_if_result, retry_if_exception_type

RETRY_COUNT = 15

CODING_SYSTEM = """
You are a helpful competitive programming assistant. The user is trying to solve a problem with your help. The user might provide you with existing ideas they have; treat these ideas as the ground truth. When asked to code, YOU MUST wrap your code in a code block, which starts and ends with "```". Your code should receive inputs from stdin and print your answer to stdout. When asked for ideas, choices or steps, ALSO wrap your response in a code block as well.
You will now be provided with the problem statement:
===
{statement}
===
"""

ALGORITHM_SYSTEM = """
You are an experienced AI assistant proficient in various programming algorithms and data structures. When provided with the name of an algorithm, you should provide accurate general steps for designing a solution. Steps should be limited to a maximum of five. Return the steps in a python list format. Use double quotes to wrap each step, and wrap the entire list in a code block.
"""

CODING_TRANSFORMATION = """
I came up with an intuition on how to solve this problem. It might be the complete solution or additional steps might be needed:
===
{transformation}
===
Analyze my intuition, how is it applicable to this problem? Please build on my idea and do not start over or reject the approach. What is the problem really asking, and how can it be solved with the algorithms and data structures you know? Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""

@retry(stop=stop_after_attempt(RETRY_COUNT), retry=(retry_if_result(lambda result: len(result[0]) == 0) | retry_if_exception_type(IndexError)))
def transformation_coder(statement: str, transformation: str, coder_mode: str) -> tuple[str, str]:
    messages = [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {
                    "role": "user",
                    "content": CODING_TRANSFORMATION.format(
                        transformation=transformation
                    ),
                },
            ]

    if coder_mode == 'gpt-4':
        coder = ChatCompletionAPI("gpt-4")
        code, response = parse_response(coder.create(messages))
    elif coder_mode.startswith('llama'):
        coder = OllamaAPI(model=coder_mode)
        code, response = parse_code_block(coder.chat(messages)), ''
    return code, response


CODING_ZEROSHOT = """
How can we break down this problem and arrive at a solution? Let's think step by step. Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""


def zeroshot_coder(statement: str, coder_mode: str = 'gpt-4') -> tuple[str, str]:
    message = [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {"role": "user", "content": CODING_ZEROSHOT},
            ]
    if coder_mode == 'gpt-4':
        coder = ChatCompletionAPI("gpt-4")
        code, response = parse_response(coder.create(message))
    elif coder_mode.startswith('llama'):
        coder = OllamaAPI(model=coder_mode)
        code, response = string_to_list(parse_code_block(coder.chat(message))), ''
    return code, response


CODING_EDITORIAL = """
According to this problem's official editorial, what are some of the intermediate variables that must be calculated? How are these variables calculated and how do they lead to an answer? Let's think step by step. In Python, please also implement the solution that can pass the most testcases, as described by the editorial.
You will now be provided with the editorial:
{editorial}
"""


def editorial_coder(statement: str, editorial: str) -> tuple[str, str]:
    coder = ChatCompletionAPI("gpt-4")
    code, response = parse_response(
        coder.create(
            [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {
                    "role": "user",
                    "content": CODING_EDITORIAL.format(editorial=editorial),
                },
            ]
        )
    )
    return code, response


CODING_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think it's a problem about {algorithm}.
Analyze my intuition, how is it applicable to this problem? Please build on my idea and do not start over or reject the approach. What is the problem really asking, and how can it be solved with the algorithms and data structures you know? Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""


def algorithm_coder(statement: str, algorithm: str, coder_mode: str) -> tuple[str, str]:
    messages = [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {
                    "role": "user",
                    "content": CODING_ALGORITHM.format(algorithm=algorithm),
                },
            ]
    if coder_mode == 'gpt-4':
        coder = ChatCompletionAPI("gpt-4")
        code, response = parse_response(coder.create(messages))
    elif coder_mode.startswith('llama'):
        coder = OllamaAPI(model=coder_mode)
        code, response = parse_code_block(coder.chat(messages)), ''
    return code, response


CODING_TRANSFORMATION_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think {transformation}. Additionally, I think it's a problem about {algorithm}.
Analyze my intuition, how is it applicable to this problem? Please build on my idea and do not start over or reject the approach. What is the problem really asking, and how can it be solved with the algorithms and data structures you know? Please implement your solution in Python and wrap your code in a code block. Remember to receive inputs from stdin and print your answer to stdout.
"""


def transformation_algorithm_coder(
    statement: str, algorithm: str, transformation: str
) -> tuple[str, str]:
    coder = ChatCompletionAPI("gpt-4")
    code, response = parse_response(
        coder.create(
            [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {
                    "role": "user",
                    "content": CODING_TRANSFORMATION_ALGORITHM.format(
                        statement=statement, algorithm=algorithm, transformation=transformation
                    ),
                },
            ]
        )
    )
    return code, response

PROVIDE_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think it's a problem about {algorithm}.
Please list concise and general steps, no more than five, for building {algorithm} program based on this problem. And return the steps in a python list format. Use double quotes to wrap each step.
"""

def provide_algorithm_coder(
    statement: str, algorithm: str, coder_mode: str
) -> tuple[str, str]:
    messages = [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {
                    "role": "user",
                    "content": PROVIDE_ALGORITHM.format(
                        statement=statement, algorithm=algorithm
                    ),
                },
            ]
    if coder_mode == 'gpt-4':
        coder = ChatCompletionAPI("gpt-4")
        code, response = parse_response_py_list(coder.create(messages))
    elif coder_mode.startswith('llama'):
        coder = OllamaAPI(model=coder_mode)
        code, response = string_to_list(parse_code_block(coder.chat(messages))), ''
    return code, response

@retry(stop=stop_after_attempt(RETRY_COUNT), retry=(retry_if_result(lambda result: len(result[0]) == 0) | retry_if_exception_type(IndexError)))
def provide_algorithm_coder2(
    algorithm: str, coder_mode: str
) -> tuple[str, str]:
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
    if coder_mode == 'gpt-4':
        coder = ChatCompletionAPI("gpt-4")
        code, response = parse_response_py_list(coder.create(messages, temperature=0.1))
    elif coder_mode.startswith('llama'):
        coder = OllamaAPI(model=coder_mode)
        code, response = string_to_list(parse_code_block(coder.chat(messages))), ''
    return code, response

FOLLOW_UP_ALGORITHM = """
I came up with an intuition on how to solve this problem. I think it's a problem about "{algorithm}".
You will provide me with three possible choices for "{step}". Each choice will be non-overlapping and independent, allowing me to choose the most suitable option later.
You must return the choices in a single python list format, which should start with \"[\" and ends with \"]\". Use double quotes(\") to wrap each choice. Your response should only contain possible choices, do not include any additional information.
YOU MUST wrap your code in a code block, which starts and ends with "```".
===BEGIN STEPS===
{steps}
===END STEPS===
"""
# Return the choices in a python list format. Use double quotes to wrap each choice.

@retry(stop=stop_after_attempt(RETRY_COUNT), retry=(retry_if_result(lambda result: len(result[0]) == 0) | retry_if_exception_type(IndexError)))
def follow_up_coder(
    statement: str, algorithm: str, step: str, steps: list[str], coder_mode: str
) -> tuple[str, str]:
    messages = [
                {
                    "role": "system",
                    "content": CODING_SYSTEM.format(statement=statement),
                },
                {
                    "role": "user",
                    "content": FOLLOW_UP_ALGORITHM.format(
                        statement=statement, algorithm=algorithm, step=step, steps='\n'.join(steps)
                    ),
                },
            ]
    
    if coder_mode == 'gpt-4':
        coder = ChatCompletionAPI("gpt-4")
        code, response = parse_response_py_list(coder.create(messages, temperature=0.8))
    elif coder_mode.startswith('llama'):
        coder = OllamaAPI(model=coder_mode)
        code, response = string_to_list(parse_code_block(coder.chat(messages))), ''
    return code, response

def attempt_usaco(
    problem: Problem,
    coder: Callable[[], tuple[str, str]],
    coder_params: dict,
    sampling_budget=5,
) -> tuple[float, list[tuple[str, str, tuple[int, int, int, int]]]]:
    code_samples = []
    full_responses = []
    results = []
    for _ in tqdm(
        range(sampling_budget), desc=f"{problem.name} ({problem.problem_id})"
    ):
        code, response = coder(**coder_params)
        code_samples.append(code)
        full_responses.append(response)
        results.append(problem.submit(code))

    score = 0
    for ac_cnt, wa_cnt, tle_cnt, re_cnt in results:
        if ac_cnt + wa_cnt + tle_cnt + re_cnt != 0:
            score = max(score, ac_cnt / (ac_cnt + wa_cnt + tle_cnt + re_cnt))

    return score, list(zip(code_samples, full_responses, results))
