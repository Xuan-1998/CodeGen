import unittest
from utils import *
import dataset
import logging
import os

codeGen_logger = logging.getLogger("Tests")
logging.basicConfig(level=logging.DEBUG)

import re

TEST_CODE = r"""def add2(list:list[int]) -> list:
    for i in range(len(list)):
        list[i] += 2
    return list

def solution(stdin_str: str) -> str:
    stdin = list(map(int, stdin_str.split()))
    stdout = add2(stdin)
    stdout_str = ' '.join(map(str, stdout))
    return stdout_str

l = input()
print(solution(l))"""

TEST_CASES = [ 
    {"stdin": "10 20 30 40 50\n", "stdout": "12 22 32 42 52\n"}, 
    {"stdin": "5 10 15\n", "stdout": "7 12 17\n"}, 
    {"stdin": "2 4 6 8 10 12 14\n", "stdout": "4 6 8 10 12 14 16\n"}, 
    {"stdin": "100 100\n", "stdout": "102 102\n"}, 
    {"stdin": "25 50 75 100 25 50\n", "stdout": "27 52 77 102 27 52\n"} 
]

PROBLEM = problems.Problem(
    statement='Problem statement',
    editorial='Editorial',
    tag='Tag',
    difficulties='Difficulties',
    source='Source',
    url='URL',
    sample_test_cases=[
        {'input': 'input1', 'output': 'output1'},
        {'input': 'input2', 'output': 'output2'}
    ]
)

@unittest.skip("Skip since it's already tested")
class TestOJInteractions(unittest.TestCase):
    def test_submit_code(self):
        token = oj_interactions.submit_code(TEST_CODE, TEST_CASES[0]["stdin"], TEST_CASES[0]["stdout"], 'local')
        pattern = r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'
        self.assertIsNotNone(token)
        self.assertTrue(re.match(pattern, token))
    
    def test_get_submission_online(self):
        token = oj_interactions.submit_code(TEST_CODE, TEST_CASES[0]["stdin"], TEST_CASES[0]["stdout"], 'online')
        submission = oj_interactions.get_submission(token, 'online')
        self.assertIn("Accepted", submission['status']["description"])

    def test_submit_code_batch(self):
        tokens = oj_interactions.submit_code_batch(TEST_CODE, TEST_CASES, 'local')
        pattern = r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'
        self.assertIsNotNone(tokens)
        for token in tokens:
            self.assertTrue(re.match(pattern, token))

@unittest.skip("Skip since it's already tested")
class TestChatbotAPI(unittest.TestCase):
    def test_chatbot(self):
        bot = chatbot.ChatCompletionAPI()
        response = bot.create(
            [
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant that helps with coding problems"
                },
                {
                    "role": "user",
                    "content": "Write a function that adds 2 to each element in a list of integers",
                },
            ]
        )
        codeGen_logger.info(response.choices[0].message.content)
        self.assertIsNotNone(response.choices[0].message.content)

    def test_embedding(self):
        embedding = chatbot.EmbeddingAPI()
        self.assertIsNotNone(embedding.embedding)

@unittest.skip("Skip since it's going to be deprecated")
class TestCodeRunner(unittest.TestCase):
    def test_code_runner(self):
        output = code_runner.code_runner(TEST_CODE, TEST_CASES[0]["stdin"])
        codeGen_logger.info(output)
        self.assertEqual(output, TEST_CASES[0]["stdout"])

@unittest.skip("Skip since it's already tested")
class TestCoding(unittest.TestCase):
    def test_transformation_algorithm_coder(self):
        code, response = coding.transformation_algorithm_coder("Given a list of integers, add 2 to each element", "List", "Add 2 to each element")
        codeGen_logger.info(response)
        self.assertIsNotNone(code)
        self.assertIsNotNone(response)

# @unittest.skip("Skip since it's already tested")
class TestProblem(unittest.TestCase):
    @unittest.skip("Skip since it's not implemented yet")
    def test_get_editorial(self):
        editorial = problems.get_editorial('URL', 'Source')
        self.assertIsNotNone(editorial)
    @unittest.skip("Skip since it's already tested")

    def test_save_and_load_problem_from_jsonl(self):
        PROBLEM.append_to_jsonl('problems.jsonl')
        PROBLEM.append_to_jsonl('problems.jsonl')
        PROBLEM.append_to_jsonl('problems.jsonl')
        
        problems_list = []
        with open('problems.jsonl', 'r') as file:
            for line in file:
                problems_list.append(problems.Problem.from_jsonl(line))

        self.assertEqual(len(problems_list), 3)
        self.assertEqual(PROBLEM.statement, problems_list[0].statement)
        self.assertEqual(PROBLEM.editorial, problems_list[0].editorial)
        self.assertEqual(PROBLEM.tag, problems_list[0].tag)
        self.assertEqual(PROBLEM.difficulties, problems_list[0].difficulties)
        self.assertEqual(PROBLEM.source, problems_list[0].source)
        self.assertEqual(PROBLEM.url, problems_list[0].url)
        self.assertEqual(PROBLEM.sample_test_cases, problems_list[0].sample_test_cases)

        # os.remove('problems.jsonl')

    def test_initialize_problems(self):
        dataset.initialize_problems(1, "Dynamic Programming")
        # pass since get_editorial is not implemented yet
        pass

if __name__ == '__main__':
    unittest.main()