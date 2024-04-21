from utils import *
from dataset import *
import os
from copy import deepcopy
import traceback
import hashlib
import json

def url_to_guid(url):
    # Create a SHA-1 hash object
    sha1 = hashlib.sha1()

    # Convert the URL string to bytes and update the hash object
    sha1.update(url.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    guid = sha1.hexdigest()

    return guid

main_logger = codeGen_logger.setup_logging()
working_directory = "/Users/jiangxuan/Desktop/09_CodeGen/CodeGen"

def main():
    main_logger.info("codeGen starts")
    # initialize_problems(100, "Dynamic Programming")
    data_path = f"{working_directory}/../data"
    # for source in os.listdir(data_path):
        # probs_path = os.path.join(data_path, source, "problems.jsonl")
    probs_path = r'/Users/yibozhao/Documents/01 Johns Hopkins/02 LLM Code Generation/CodeGen/data/easyDP.jsonl'
    with open(probs_path, 'r') as file:
        for line in file:
            prob = problems.Problem.from_jsonl(line)
            main_logger.info(f"Processing problem {prob.url}")
            lis, response = coding.provide_algorithm_coder(prob.statement, "Dynamic Programming")
            main_logger.info(f"Algorithm: {lis}")
            steps_queue = []
            steps_queue.append([[lis[0]], lis[1:]])
            codes = []
            # [step, previous step] -> new [step, previous step], add to queue
            # Eg. 5 choices ABCDE -> A1BCDE, A2BCDE, A3BCDE -> A1B1CDE, A1B2CDE, A1B3CDE, A2B1CDE, A2B2CDE, A2B3CDE, A3B1CDE, A3B2CDE, A3B3CDE
            # iter until previous step is empty and then gen code
            # iter until queue is empty
            while steps_queue:
                try:
                    step, steps_to_generate = steps_queue.pop(0)
                    if len(steps_to_generate) == 0:
                        # TODO: Might change the statement+transformation gen code func here
                        # Not tested
                        code, response = coding.transformation_coder(prob.statement, "\n".join(step))
                        codes.append(code)
                        continue
                    # Tested but LLM gen not stable, sometimes works well sometimes not
                    # TODO refine the prompts
                    lis, response = coding.follow_up_coder(prob.statement, "Dynamic Programming", steps_to_generate[0], step + steps_to_generate)
                    main_logger.info(f"Step: {steps_to_generate[0]} Choices: {lis}")
                    steps_to_generate.pop(0)
                    for choice in lis:
                        current_step = deepcopy(step)
                        current_step.append(choice)
                        steps_queue.append([current_step, steps_to_generate])
                except Exception as e:
                    main_logger.error(f"An error occurred: {e}, {steps_to_generate}, {traceback.format_exc()}")
                    
            main_logger.info(f"Codes num: {len(codes)}")
            main_logger.debug(f"Codes: {codes}")

            folderName = url_to_guid(prob.url)[:8]
            subFolderName = f'results/{folderName}'
            if not os.path.exists(subFolderName):
                os.makedirs(subFolderName)

            test_cases = []
            for test_case in prob.sample_test_cases:
                inputs = "\n".join(map(str, test_case['input'])) if isinstance(test_case['input'], list) else str(test_case['input'])
                if not inputs.endswith("\n"):
                    inputs += "\n"
                outputs = "\n".join(map(str, test_case['output'])) if isinstance(test_case['output'], list) else str(test_case['output'])
                # if not outputs.endswith("\n"):
                #     outputs += "\n"
                test_cases.append({
                    "input": inputs,
                    "output": outputs
                })

            with open(f"{subFolderName}/test.json", 'w') as json_file:
                json.dump(test_cases, json_file, indent=4)
                main_logger.info(f"Test cases length: {len(test_cases)}")
                main_logger.debug(f"Test cases: {test_cases}")

            # iterate
            for index, entry in enumerate(codes):
                # name       
                filename = f'{subFolderName}/code_{index}.py'            
                # open new file
                with open(filename, 'w') as file:
                    # print entry
                    print(entry, file=file)
                    file.close()
                    main_logger.debug(f"Code: {entry}")

if __name__ == "__main__":
    main()