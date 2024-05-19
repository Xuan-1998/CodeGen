from utils import *
from dataset import *
import os
from copy import deepcopy
from typing import Callable
import traceback
import json
from tenacity import RetryError
from utils.prompts import DYNAMIC_PROGRAMMING

main_logger = codeGen_logger.setup_logging()
# CHATBOT = chatbot.ChatCompletionAPI(model="gpt-4")
CHATBOT = chatbot.OllamaAPI(model="llama3")

# tree search version 1 - genreral steps
# tree search version llama - use llama instead of gpt4
# tree search version 2 - with defined steps
# tree search version 3 - with defined steps and evaluation steps
# tree search version 4 - refine prompts
def tree_search_4_medium_hard(prob: Problem)->list[str]:
    coder = coding.Coding(prob.statement, CHATBOT)
    algorithm = "Dynamic Programming" #prob.tag.strip().split(', ')[0]
    # general_steps, _ = coding.provide_algorithm_coder2(algorithm, CHAT_MODE)
    general_steps = DYNAMIC_PROGRAMMING
    main_logger.info(f"Algorithm: {algorithm}, General steps: {general_steps}")

    steps_queue = []
    steps_queue.append([[], general_steps])
    codes = []
    transformations = []
    # [step, previous step] -> new [step, previous step], add to queue
    # Eg. 5 choices ABCDE -> A1BCDE, A2BCDE, A3BCDE -> A1B1CDE, A1B2CDE, A1B3CDE, A2B1CDE, A2B2CDE, A2B3CDE, A3B1CDE, A3B2CDE, A3B3CDE
    # iter until previous step is empty and then gen code
    # iter until queue is empty
    while steps_queue:
        [step, steps_to_generate] = steps_queue.pop(0)
        main_logger.info(f"POP0: Queue Length: {len(steps_queue)}, Current steps: {step}, Steps to generate: {steps_to_generate}")
        if len(steps_to_generate) == 0:
            transformation = "\n".join(step)
            try:
                main_logger.info(f"Starting transformation evaluation: Transformation: {transformation}")
                evaluated_transformation, response = coder.evaluation_coder(algorithm, transformation)
                main_logger.info(f"Starting code generation: Transformation: {evaluated_transformation}")
                main_logger.debug(f"Starting code genration: Original repsonse: {response}")
                code, response = coder.transformation_coder(evaluated_transformation)
                main_logger.debug(f"Code generation response: {response}")
            except RetryError as e:
                main_logger.error(f"An error occurred: {e}, {transformation}, {traceback.format_exc()}")
                
            codes.append(code)
            transformations.append(evaluated_transformation)
            continue

        main_logger.info(f"Start following up: {steps_to_generate[0]}, Coder: {CHATBOT.__class__.__name__}")

        try:
            lis, response = coder.follow_up_coder(algorithm, steps_to_generate[0], step + steps_to_generate)
            main_logger.debug(f"Follow up response: {response}")
        except RetryError as e:
            lis = [steps_to_generate[0]]
            main_logger.error(f"An error occurred: {e}, {steps_to_generate}, {traceback.format_exc()}")

        main_logger.info(f"Step: {steps_to_generate[0]} Choices: {lis}")

        for choice in lis:
            current_step = deepcopy(step)
            current_step_to_generate = steps_to_generate[1:]
            current_step = current_step + [choice]
            steps_queue.append([current_step, current_step_to_generate])

    return codes, transformations

def zero_shot(prob: Problem, sample_budget: int = 10)->list[str]:
    codes = []
    coder = coding.Coding(prob.statement, CHATBOT)
    while len(codes) < sample_budget:
        try:
            code, _ = coder.zeroshot_coder()
            codes.append(code)
            main_logger.info(f"Zero-shot length: {len(codes)}/{sample_budget}")
            main_logger.debug(f"Zero-shot code: {code}")
        except Exception as e:
            main_logger.error(f"An error occurred: {e}, {traceback.format_exc()}")

    return codes

# Prevent repeatedly generating code with same baseline strategy
def get_sample_budget(prob: Problem, baseline_name: str, total_budget: int)->int:
    subFolderName = f'results/{baseline_name}/{prob.get_prob_guid()[:8]}'
    if not os.path.exists(subFolderName):
        return total_budget
    else:
        current_count = len([name for name in os.listdir(subFolderName) if name.startswith("code_")])
        return total_budget - current_count

def save_results(prob: Problem, folderName: str, codes: list[str], transformations: list[str] = None):    
    subFolderName = f'results/{folderName}/{prob.get_prob_guid()[:8]}'
    if not os.path.exists(subFolderName):
        os.makedirs(subFolderName)

    if transformations is not None and len(codes) != len(transformations):
        main_logger.error(f"Code count should equal to transformation count: Code count: {len(codes)}, Transformation count: {len(transformations)}")
        with open(f"{subFolderName}/transformation.txt", 'w') as file:
            print(transformations, file=file)
        transformations = None

    test_cases = []
    for test_case in prob.sample_test_cases:
        inputs = "\n".join(map(str, test_case['input'])) if isinstance(test_case['input'], list) else str(test_case['input'])
        if not inputs.endswith("\n"):
            inputs += "\n"
        outputs = "\n".join(map(str, test_case['output'])) if isinstance(test_case['output'], list) else str(test_case['output'])
        test_cases.append({
            "input": inputs,
            "output": outputs
        })

    with open(f"{subFolderName}/test.json", 'w') as json_file:
        json.dump(test_cases, json_file, indent=4)
        main_logger.info(f"Test cases length: {len(test_cases)}")
        main_logger.debug(f"Test cases: {test_cases}")
    with open(f"{subFolderName}/prob.json", 'w') as json_file:
        json.dump(prob.to_json(), json_file, indent=4)
        main_logger.debug(f"Problem: {prob}")

    for index, entry in enumerate(codes):
        filename = f'{subFolderName}/code_{index}.py'            
        with open(filename, 'w') as file:
            print(entry, file=file)
        main_logger.debug(f"Code: {entry}")
        if transformations is not None:
            filename = f'{subFolderName}/transformation_{index}.txt'
            with open(filename, 'w') as file:
                print(transformations[index], file=file)

def codeGen(
        data_path: str = "../data/mix-100", 
        codeGen_strategy: Callable[[Problem], tuple[list[str], list[str]]] = tree_search_4_medium_hard,
        baseline_strategy: Callable[[Problem, int], list[str]] = zero_shot
    ):
    main_logger.info("codeGen starts")
    # for source in os.listdir(data_path):
    #     if os.path.isdir(os.path.join(data_path, source)) is False and source.endswith(".jsonl"):
    #         probs_path = os.path.join(data_path, source)
    #     else:
    probs_path = os.path.join(r"../data/balanced-probs-dp/medium_hard/problems.jsonl")
    with open(probs_path, 'r') as file:
        for line in file:
            prob = problems.Problem.from_jsonl(line)
            if prob.url is None:
                continue
            prob_guid = prob.get_prob_guid()[:8]
            main_logger.info(f"Processing problem {prob.url}, GUID: {prob_guid}")
            # skip if already generated.
            prob_save_path = f'results/{codeGen_strategy.__name__}/{prob_guid}'
            if os.path.exists(prob_save_path):# and prob_guid in os.listdir(
                #f"results/{codeGen_strategy.__name__}/{prob.get_prob_guid()[:8]}"
           # ):
                continue
            codes, transformations = codeGen_strategy(prob)
            main_logger.info(f"Strategy:{codeGen_strategy.__name__}, Generated code count: {len(codes)}")
            main_logger.debug(f"Codes: {codes}")
            if len(codes) == 0:
                main_logger.error(f"Code generation failed for {prob.url}")
                continue
            save_results(prob, codeGen_strategy.__name__, codes, transformations)

            sample_budget = get_sample_budget(prob, baseline_strategy.__name__, len(codes))
            codes = baseline_strategy(prob, sample_budget)
            main_logger.info(f"Baseline:{baseline_strategy.__name__}, Generated code count: {len(codes)}")
            main_logger.debug(f"Codes: {codes}")
            save_results(prob, baseline_strategy.__name__, codes)


if __name__ == "__main__":
    # working_directory = "/Users/jiangxuan/Desktop/09_CodeGen/CodeGen"
    # data_path = f"{working_directory}/data"
    # codeGen(data_path)
    codeGen(data_path="../data/balanced-probs",codeGen_strategy=tree_search_4_medium_hard, baseline_strategy=zero_shot)
