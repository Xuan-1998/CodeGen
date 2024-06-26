import requests
import logging
import os
import json
import base64

logger = logging.getLogger("__name__")

BASE_URL = {
    "local": "http://localhost:2358",
    "online": "https://judge0-ce.p.rapidapi.com",
}

HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY", ""),
    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
}

QUERY_PARAMS = {"base64_encoded": "false", "fields": "*"}


# method: local or online
# TODO: currently only supports online, investigating the problem with local server
def submit_code(code: str, stdin: str, stdout: str, method="local") -> str:
    language_id = {"local": 71, "online": 92}  # python

    payload = {
        "language_id": language_id[method],
        "source_code": code,
        "stdin": stdin,
        "expected_output": stdout,
    }

    url = f"{BASE_URL[method]}/submissions"
    logger.debug(f"Payload: {payload}")

    response = requests.post(url, json=payload, headers=HEADERS, params=QUERY_PARAMS)
    token = response.json()["token"]
    logger.info(f"Token: {token}")

    return token


def submit_code_batch(code: str, test_cases: list[dict], method="local") -> list[str]:
    language_id = {"local": 71, "online": 92}  # python

    payload = {"submissions": []}

    for test_case in test_cases:
        inputs = (
            "\n".join(test_case["input"])
            if type(test_case["input"]) is list
            else test_case["input"]
        )
        if not inputs.endswith("\n"):
            inputs += "\n"
        outputs = (
            "\n".join(test_case["output"])
            if type(test_case["output"]) is list
            else test_case["output"]
        )
        if not outputs.endswith("\n"):
            outputs += "\n"

        payload["submissions"].append(
            {
                "language_id": language_id[method],
                "source_code": code,
                "stdin": inputs,
                "expected_output": outputs,
            }
        )

    url = f"{BASE_URL[method]}/submissions/batch"
    logger.debug(f"Payload: {payload}")

    try:
        response = requests.post(url, json=payload, headers=HEADERS, params=QUERY_PARAMS)
        response_data = response.json()
        if isinstance(response_data, list):
            tokens = [item["token"] for item in response_data]
        else:
            if response.status_code != 200:
                logger.error(
                    f"HTTP Error: {response.status_code} with body {response.text}"
                )
                return []
            logger.error(f"Unexpected JSON structure: {response_data}")
            return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON decoding failed: {str(e)}")
        return []
    except KeyError as e:
        logger.error(f"KeyError: {str(e)}")
        return []
    except:
        logger.error(f"Error: {str(e)}")
        return []
    
    logger.info(f"Tokens: {tokens}")

    return tokens


def get_submission(token: str, method="local"):
    url = f"{BASE_URL[method]}/submissions/{token}"
    try:
        response = requests.get(url, params=QUERY_PARAMS, headers=HEADERS)
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return None
    
    if response.status_code != 200:
        logger.error(f"Error: {response.status_code}, {response.json()}")
        return None
    # print(response.json())
    logger.info(
        f"Response: Token: {response.json()['token']}, Description: {response.json()['status']['description']}"
    )
    return response.json()


def get_status_and_output(response: str):
    if not response:
        return "No response", "No response"
    try:
        decoded_bytes = base64.b64decode(response["stdout"])
        decoded_str = decoded_bytes.decode('latin-1')
    except:
        decoded_str = response["stdout"]
    return response["status"]["description"], decoded_str


def submit_officially(code: str, stdin: str, stdout: str) -> dict:
    # placeholder, will submit code to leetcode/codeforce, https://github.com/Sajantoor/LeetCode-API?tab=readme-ov-file
    # https://github.com/online-judge-tools/api-client - It's possible to use this API to submit code to various OJs or get system cases
    # References provided by ALGO:
    #  - [python-leetcode](https://github.com/fspv/python-leetcode)
    #  - [CodeforcesApiPy](https://github.com/VadVergasov/CodeforcesApiPy)
    #  - [codeforces-problem-scraper-api](https://github.com/kerolloz/codeforces-problem-scraper-api/tree/master)
    # For overall testing / Or maybe just use the method used in ALGO
    pass
