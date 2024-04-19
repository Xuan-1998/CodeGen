import requests
import logging
import os

logger = logging.getLogger("__name__") 

BASE_URL = {
    'local': "http://localhost:2358",
    'online': "https://judge0-ce.p.rapidapi.com"
}

HEADERS = {
    'Content-Type': 'application/json',
    'X-RapidAPI-Key': os.environ.get('RAPIDAPI_KEY', ''),
    'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com'
}

QUERY_PARAMS = {
    'base64_encoded': 'false',
    'fields': '*'
}

# method: local or online
# TODO: currently only supports online, investigating the problem with local server
def submit_code(code: str, stdin: str, stdout: str, method = 'local') -> str:
    language_id = {
        'local': 71,
        'online': 92
    } # python

    payload = {
        "language_id": language_id[method],
        "source_code": code,
        "stdin": stdin,
        "expected_output": stdout
    }

    url = f"{BASE_URL[method]}/submissions"
    logger.debug(f"Payload: {payload}")

    response = requests.post(url, json=payload, headers=HEADERS, params=QUERY_PARAMS)
    token = response.json()['token']
    logger.info(f"Token: {token}")
    
    return token

def submit_code_batch(code: str, test_cases: list[dict], method = 'local') -> list[str]:
    language_id = {
        'local': 71,
        'online': 92
    } # python

    payload = {
        "submissions":[]
    }

    for test_case in test_cases:
        inputs = "\n".join(test_case['input']) if type(test_case['input']) is list else test_case['input']
        if not inputs.endswith("\n"):
            inputs += "\n"
        outputs = "\n".join(test_case['output']) if type(test_case['output']) is list else test_case['output']
        if not outputs.endswith("\n"):
            outputs += "\n"

        payload['submissions'].append({
            "language_id": language_id[method],
            "source_code": code,
            "stdin": inputs,
            "expected_output": outputs
        })

    url = f"{BASE_URL[method]}/submissions/batch"
    logger.debug(f"Payload: {payload}")

    response = requests.post(url, json=payload, headers=HEADERS, params=QUERY_PARAMS)
    tokens = [item['token'] for item in response.json()]
    logger.info(f"Tokens: {tokens}")
    
    return tokens

def get_submission(token: str, method = 'local'):
    url = f"{BASE_URL[method]}/submissions/{token}"
    response = requests.get(url, params=QUERY_PARAMS, headers=HEADERS)
    if response.status_code != 200:
        logger.error(f"Error: {response.status_code}, {response.json()}")
    print(response.json())
    logger.debug(f"Response: Token: {response.json()['token']}, Description: {response.json()['status']['description']}")
    return response.json()

def submit_officially(code: str, stdin: str, stdout: str) -> dict:
    # placeholder, will submit code to leetcode/codeforce, https://github.com/Sajantoor/LeetCode-API?tab=readme-ov-file
    # https://github.com/online-judge-tools/api-client - It's possible to use this API to submit code to various OJs or get system cases
    # References provided by ALGO:
    #  - [python-leetcode](https://github.com/fspv/python-leetcode)
    #  - [CodeforcesApiPy](https://github.com/VadVergasov/CodeforcesApiPy)
    #  - [codeforces-problem-scraper-api](https://github.com/kerolloz/codeforces-problem-scraper-api/tree/master)
    # For overall testing / Or maybe just use the method used in ALGO
    pass
