import logging
import json
import hashlib

logger = logging.getLogger("__name__")

class Problem:
    def __init__(
            self, 
            statement: str, 
            editorial: str,
            tag: str,
            difficulties: str,
            source: str,
            url: str,
            sample_test_cases: list[dict] = []
        ):
        self.statement = statement
        self.editorial = editorial
        self.tag = tag
        self.difficulties = difficulties
        self.source = source
        self.url = url
        self.sample_test_cases = sample_test_cases

    def submit(self, code: str, stdin: str, stdout: str, method = 'local') -> str:
        from .oj_interactions import submit_code, get_submission
        token = submit_code(code, stdin, stdout, method)
        response = get_submission(token, method)
        return response['status']['description'] if response else 'Getting response failed'
        
    def submit_batch(self, code: str, test_cases: list[dict], method = 'local') -> list[str]:
        from .oj_interactions import submit_code_batch, get_submission
        tokens = submit_code_batch(code, test_cases, method)
        responses = []
        for token in tokens:
            response = get_submission(token, method)
            description = response['status']['description'] if response else 'Getting response failed'
            responses.append(description)
        return responses
    
    def to_json(self):
        return json.dumps(self.__dict__)

    def append_to_jsonl(self, file_path):
        with open(file_path, 'a') as file:
            file.write(self.to_json() + '\n')

    def get_prob_guid(self):
        sha1 = hashlib.sha1()
        sha1.update(self.url.encode('utf-8'))
        guid = sha1.hexdigest()
        return guid

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

    @classmethod
    def from_jsonl(cls, jsonl_str):
        problem = cls.from_json(jsonl_str)
        return problem
    

def get_editorial(url: str, source: str) -> str:
    editorial = ""
    logger.info(f"Getting editorial from {source} at {url}")
    # TODO: Implement this function
    logger.info(f"Editorial: {editorial}")
    return editorial
