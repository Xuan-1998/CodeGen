from utils import *
from dataset import *
import os
from copy import deepcopy
from typing import Callable
import traceback
import json

main_logger = codeGen_logger.setup_logging()

# tree search version 1 - genreral steps
def tree_search_1(prob: Problem)->list[str]:
    algorithm = prob.tag.strip().split(', ')[0]
    # lis, _ = coding.provide_algorithm_coder(prob.statement, algorithm)
    lis, _ = coding.provide_algorithm_coder2(algorithm)
    main_logger.info(f"Algorithm: {algorithm}, General steps: {lis}")

    steps_queue = []
    steps_queue.append([[lis[0]], lis[1:]])
    codes = []
    transformations = []
    # [step, previous step] -> new [step, previous step], add to queue
    # Eg. 5 choices ABCDE -> A1BCDE, A2BCDE, A3BCDE -> A1B1CDE, A1B2CDE, A1B3CDE, A2B1CDE, A2B2CDE, A2B3CDE, A3B1CDE, A3B2CDE, A3B3CDE
    # iter until previous step is empty and then gen code
    # iter until queue is empty
    while steps_queue:
        try:
            step, steps_to_generate = steps_queue.pop(0)
            if len(steps_to_generate) == 0:
                transformation = "\n".join(step)
                code, _ = coding.transformation_coder(prob.statement, transformation)
                codes.append(code)
                transformations.append(transformation)
                continue

            lis, _ = coding.follow_up_coder(prob.statement, algorithm, steps_to_generate[0], step + steps_to_generate)
            main_logger.info(f"Step: {steps_to_generate[0]} Choices: {lis}")

            steps_to_generate.pop(0)

            for choice in lis:
                current_step = deepcopy(step)
                current_step.append(choice)
                steps_queue.append([current_step, steps_to_generate])

        except Exception as e:
            main_logger.error(f"An error occurred: {e}, {steps_to_generate}, {traceback.format_exc()}")

    return codes, transformations

def zero_shot(prob: Problem, sample_budget: int = 10)->list[str]:
    codes = []
    while len(codes) < sample_budget:
        try:
            code, _ = coding.zeroshot_coder(prob.statement)
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
        codeGen_strategy: Callable[[Problem], tuple[list[str], list[str]]] = tree_search_1,
        baseline_strategy: Callable[[Problem, int], list[str]] = zero_shot
    ):
    main_logger.info("codeGen starts")
    for source in os.listdir(data_path):
        if os.path.isdir(os.path.join(data_path, source)) is False and source.endswith(".jsonl"):
            probs_path = os.path.join(data_path, source)
        else:
            probs_path = os.path.join(data_path, source, "problems.jsonl")
        with open(probs_path, 'r') as file:
            for line in file:
                prob = problems.Problem.from_jsonl(line)
                if prob.url is None:
                    continue
                prob_guid = prob.get_prob_guid()[:8]
                main_logger.info(f"Processing problem {prob.url}, GUID: {prob_guid}")

                codes, transformations = codeGen_strategy(prob)
                main_logger.info(f"Strategy:{codeGen_strategy.__name__}, Generated code count: {len(codes)}")
                main_logger.debug(f"Codes: {codes}")
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
    codeGen(data_path="../data/mix-100",codeGen_strategy=tree_search_1, baseline_strategy=zero_shot)