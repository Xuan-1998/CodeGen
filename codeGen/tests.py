import unittest
from utils import *
import dataset
import logging
import os
import time

codeGen_logger = logging.getLogger("Tests")
logging.basicConfig(level=logging.DEBUG)

import re

TEST_CODE = r"""def add2(list:list[int]) -> list:
    for i in range(len(list)):
        list[i] += 2
    return list

def solution(input_str: str) -> str:
    input = list(map(int, input_str.split()))
    output = add2(input)
    output_str = ' '.join(map(str, output))
    return output_str

l = input()
print(solution(l))"""

TEST_CASES = [ 
    {"input": "10 20 30 40 50\n", "output": "12 22 32 42 52\n"}, 
    {"input": "5 10 15\n", "output": "7 12 17\n"}, 
    {"input": "2 4 6 8 10 12 14\n", "output": "4 6 8 10 12 14 16\n"}, 
    {"input": "100 100\n", "output": "102 102\n"}, 
    {"input": "25 50 75 100 25 50\n", "output": "27 52 77 102 27 52\n"} 
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

TEST_STATEMENT = [{'role': 'system', 'content': '\nYou are a helpful competitive programming assistant. The user is trying to solve a problem with your help. The user might provide you with existing ideas they have; treat these ideas as the ground truth. When asked to code, you must wrap your code in a code block. Your code should receive inputs from stdin and print your answer to stdout. When asked for ideas, choices or steps, you must wrap your response in a code block, which starts and ends with \"```\".\nYou will now be provided with the problem statement:\n===\nTask: Given the number of passes N and the number of players K, find the number of ways the ball can be passed between the players such that Lionel Messi receives the ball after exactly N passes. The output should be the number of ways modulo 1000000007.\n\nInput: The input consists of T test cases. The first line of each test case contains two integers N and K. \n\nOutput: For each test case, output a single integer, the number of ways the winning play might happen modulo 1000000007.\n\nConstraints: 1 ≤ T ≤ 100, 2 ≤ N ≤ 1000, and 1 ≤ K ≤ 10.\n===\n'}, {'role': 'user', 'content': "\nI came up with an intuition on how to solve this problem. I think it's a problem about ['Dynamic programming'.\nYou will provide me with three possible choices for Define the problem and identify the recursive relation. Each choice will be parallel and independent, allowing me to choose the most suitable option later.\nYou must return the choices in a single python list format, which should start with \"[\" and ends with \"]\". Use double quotes(\") to wrap each choice. \n===BEGIN STEPS===\nDefine the problem and identify the recursive relation\nDetermine the base cases for the recursion\nFind the overlapping subproblems and optimize using memoization or tabulation\nImplement the dynamic programming algorithm to solve the problem\nOptimize and refine the solution as needed\n===END STEPS===\n"}]

@unittest.skip("Skip since it's already tested")
class TestOJInteractions(unittest.TestCase):
    def test_submit_code(self):
        token = oj_interactions.submit_code(TEST_CODE, TEST_CASES[0]["input"], TEST_CASES[0]["output"], 'local')
        pattern = r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'
        self.assertIsNotNone(token)
        self.assertTrue(re.match(pattern, token))
    
    def test_get_submission_online(self):
        token = oj_interactions.submit_code(TEST_CODE, TEST_CASES[0]["input"], TEST_CASES[0]["output"], 'online')
        time.sleep(5)
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
        output = code_runner.code_runner(TEST_CODE, TEST_CASES[0]["input"])
        codeGen_logger.info(output)
        self.assertEqual(output, TEST_CASES[0]["output"])

@unittest.skip("Skip since it's already tested")
class TestCoding(unittest.TestCase):
    def test_transformation_algorithm_coder(self):
        code, response = coding.transformation_algorithm_coder("Given a list of integers, add 2 to each element", "List", "Add 2 to each element")
        codeGen_logger.info(response)
        self.assertIsNotNone(code)
        self.assertIsNotNone(response)

class TestOllama(unittest.TestCase):
    @unittest.skip("Skip since it's already tested")
    def test_chat(self):
        ollama = chatbot.OllamaAPI()
        response = ollama.chat(messages=
            [
                {
                    'role': 'system',
                    'content': coding.ALGORITHM_SYSTEM,
                },
                {
                    'role': 'user',
                    'content': 'Dynamic Programming',
                },
            ]
        )
        codeGen_logger.info(response)
        list_response = chatbot.string_to_list(chatbot.parse_code_block(response))
        codeGen_logger.info(list_response)
        self.assertIsNotNone(list_response)

    def test_response_format(self):
        coder = chatbot.OllamaAPI(model="llama3")
        code = chatbot.string_to_list(chatbot.parse_code_block(coder.chat(TEST_STATEMENT)))
        codeGen_logger.info(code)
        self.assertGreaterEqual(len(code), 1)


@unittest.skip("Skip since it's already tested")
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

        os.remove('problems.jsonl')

    def test_initialize_problems(self):
        dataset.initialize_problems(1, "Dynamic Programming")
        # pass since get_editorial is not implemented yet
        pass

if __name__ == '__main__':
    unittest.main()