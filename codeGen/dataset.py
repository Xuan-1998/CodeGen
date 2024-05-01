from utils.chatbot import ChatCompletionAPI
from utils.codeGen_logger import setup_logging
from utils.problems import Problem, get_editorial
from prompts import *
import os
import json
from datasets import load_dataset
import traceback

ds = load_dataset("BAAI/TACO", split="train")
logger = setup_logging()

MAX_SAMPLE_TC = 15

STATEMENT_SYSTEM = """
You are a competitive programming teacher. The user will provide you with the problem statement of a competitive programming problem. Your task is to summarize the problem in an abstract way. In the first paragraph of your response, summarize the task. In the second paragraph, summarize the input format and make sure to mention that input arrives from standard input. In the third paragraph, summarize the output format. In the fourth paragraph, include relevant input constraints.
"""

STATEMENT_REGULARIZATION = """
Please summarize this competitive programming problem statement: %s
"""

STATEMENT_POTSPROCESS = """
Now, redefine and abstract the problem in terms of mathematical and computer science concepts (e.g. integers, strings, number lines, sequences, graphs, trees, positions on grid) while keeping the format. As I said before, you are encouraged to use as much math language as possible to replace flavor text. You can remove all background stories, but if the task involves satisfying certain conditions with certain operations, you must explain both the operations permitted and the conditions to satisfy clearly.
Here is a good example:
Task: "There are N vertices and M edges on a graph. The cost of adding an edge between vertex i and j is (i-j^2. Add up to two new edges so that vertex 1 and vertex N become connected. What is the minimum cost to achieve that?"
Intput: "The first line of input contains T. Each test case starts with two integers, N and M, followed by M lines, each containing two integers i and j, representing a path between two different vertices i and j. It is guaranteed that there is at most one path between any two vertices, and the sum of N+M over all test cases is at most 5 * 10^5.
."
Output: "The output should consist of T lines. Each line should contain a single integer giving the minimum cost for the corresponding test case."
Constraints: "$1\le N\le 10^5$; $0\le M\le 10^5$; $1\le T\le 20$"
"""

EDITORIAL_SYSTEM = """
You are a competitive programming teacher. The user has abstracted a competitive programming problem by describing it with computer science and mathematical concepts. The user will provide you with the editorial of the original analysis and ask you questions. When responding, make sure your response align with the concepts described in the abstracted statement.
The original problem statement:
%s
The abstracted problem statement:
%s 
"""

EDITORIAL_REGULARIZATION = """
Step by step, please summarize the approach described in this editorial. Make sure your response align with the abstracted problem statement. Respond with one paragraph containing the numbered step. Here is the editorial: %s
"""

EDITORIAL_ALGORITHM = """
From a list of tags containing algorithms, data structures, or problem solving paradigms, select the single most relevant one according to the original editorial and the abstracted version you just generated. You must only pick one tag. Respond with only the tag in one line and NOTHING ELSE. Here is the list to pick from: %s
"""

EDITORIAL_TRANSFORMATION = """
According to the abstracted editorial you generated, what intuitions we must have to transform the abstract problem into a problem about %s so that it can be solved with relevant algorithms? How do you know we can apply these transformations? In a concise paragraph containing no more than one sentence, respond by filling in the blanks: "Due to the what special properties, we can transform the problem by what, redefining it into what". Without exceeding the sentence limit, be as specific as possible. You do not need to code.
"""

def regularize_statement_3(problem: Problem):
    chat = ChatCompletionAPI("gpt-3.5-turbo")
    summary = chat.create(
        [
            {"role": "system", "content": STATEMENT_SYSTEM},
            {"role": "user", "content": STATEMENT_REGULARIZATION % problem.statement},
        ],
        temperature=0.3
    ).choices[0].message.content

    return chat.create(
        [
            {"role": "system", "content": STATEMENT_SYSTEM},
            {"role": "user", "content": STATEMENT_REGULARIZATION % problem.statement},
            {"role": "assistant", "content": summary},
            {"role": "user", "content": STATEMENT_POTSPROCESS},
        ],
        temperature=0.3
    ).choices[0].message.content


def regularize_editorial_3(
    original_problem: Problem, regularized_statement: str
):
    chat = ChatCompletionAPI("gpt-3.5-turbo-16k")
    editorial = chat.create(
        [
            {
                "role": "system",
                "content": EDITORIAL_SYSTEM
                % (original_problem.statement, regularized_statement),
            },
            {
                "role": "user",
                "content": EDITORIAL_REGULARIZATION % original_problem.editorial,
            },
        ],
        temperature=0.3,
    ).choices[0].message.content

    if not hasattr(original_problem, "tags"):
        tags = TAG
    else:
        tags = original_problem.tags

    algorithm = chat.create(
        [
            {
                "role": "system",
                "content": EDITORIAL_SYSTEM
                % (original_problem.statement, regularized_statement),
            },
            {
                "role": "user",
                "content": EDITORIAL_REGULARIZATION % original_problem.editorial,
            },
            {"role": "assistant", "content": editorial},
            {"role": "user", "content": EDITORIAL_ALGORITHM % tags},
        ],
        temperature=0.3,
    ).choices[0].message.content

    transformation = chat.create(
        [
            {
                "role": "system",
                "content": EDITORIAL_SYSTEM
                % (original_problem.statement, regularized_statement),
            },
            {
                "role": "user",
                "content": EDITORIAL_REGULARIZATION % original_problem.editorial,
            },
            {"role": "assistant", "content": editorial},
            {"role": "user", "content": EDITORIAL_ALGORITHM % tags},
            {"role": "assistant", "content": algorithm},
            {"role": "user", "content": EDITORIAL_TRANSFORMATION % algorithm},
        ],
        temperature=0.3,
    ).choices[0].message.content
    return f"""Algorithm: {algorithm}

Transformation: {transformation}

Editorial: 
{editorial}"""


def initialize_problems(
        maxSize: int = 1000,
        tag: str = None,
        prefered_sources: list[str] = None,
        difficulty: str = None,
        root: str = "../data"
        ):
    cnt = 0
    for sample in iter(ds):
        if cnt >= maxSize:
            break

        if (tag is not None and tag.lower() not in (sample['tags']).lower()) or \
            (prefered_sources is not None and sample['source'] not in prefered_sources) or \
            (difficulty is not None and difficulty.lower() not in (sample['difficulty']).lower()) or sample['url'] is None or len(sample['tags']) == 0:
            continue
        
        difficulty_tag = sample['difficulty'].lower()
        cnt += 1

        logger.info(f"Processing problem {cnt} with source {sample['source']}")
        if not os.path.exists(f"{root}/{difficulty_tag}"):
            os.makedirs(f"{root}/{difficulty_tag}")

        test_cases = []
        try:
            tc_json = json.loads(sample['input_output'])
            for i in range(min(len(tc_json['inputs']), MAX_SAMPLE_TC)):
                test_cases.append({
                    'input': tc_json['inputs'][i],
                    'output': tc_json['outputs'][i]
                })

            prob = Problem(
                statement = sample['question'],
                editorial = get_editorial(sample['url'], sample['source']) if 'url' in sample else None,
                tag = sample['tags'] if 'tags' in sample else None,
                difficulties = sample['difficulty'],
                source = sample['source'],
                url = sample['url'] if 'url' in sample else None,
                sample_test_cases = test_cases
            )
            logger.debug(f"Problem: {prob.to_json()}")

            logger.info(f"Cnt: {cnt}, Regularizing problem {cnt} source {sample['source']}, url: {sample['url']}")
            # TODO: Improve with parallel processing like Task.WhenAll in .NET
            regularized_statement = regularize_statement_3(prob)
            # regularized_editorial = regularize_editorial_3(prob, regularized_statement)

            prob.statement = regularized_statement
            # prob.editorial = regularized_editorial

            # TODO: On second thought, store the problems in separate files is better
            # Hash the prob URL as GUID
            prob.append_to_jsonl(f"{root}/{difficulty_tag}/problems.jsonl")
        except Exception as e:
            logger.error(f"Error processing problem {cnt} with source {sample['source']}, url: {sample['url']}: {e}, {traceback.format_exc()}")
            continue

if __name__ == "__main__":
    initialize_problems(200, root="../data/balanced-probs-dp", tag="Dynamic Programming", difficulty="MEDIUM")
    # initialize_problems(1000, "Dynamic Programming")