from utils import *
from dataset import *
import os
from copy import deepcopy

main_logger = codeGen_logger.setup_logging()
working_directory = "/Users/jiangxuan/Desktop/09_CodeGen/CodeGen"

def main():
    main_logger.info("codeGen starts")
    # initialize_problems(100, "Dynamic Programming")
    data_path = f"{working_directory}/data"
    for source in os.listdir(data_path):
        probs_path = os.path.join(data_path, source, "problems.jsonl")
        with open(probs_path, 'r') as file:
            for line in file:
                prob = problems.Problem.from_jsonl(line)
                main_logger.info(f"Processing problem {source} {prob.url}")
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
                        step, prev_steps = steps_queue.pop(0)
                        if not prev_steps:
                            # TODO: Might change the statement+transformation gen code func here
                            # Not tested
                            code = coding.transformation_coder(prob.statement, " ".join(step))
                            codes.append(code)
                        # Tested but LLM gen not stable, sometimes works well sometimes not
                        # TODO refine the prompts
                        if prev_steps and len(prev_steps) > 0:
                            lis, response = coding.follow_up_coder(prob.statement, "Dynamic Programming", prev_steps[0], step)
                            prev_steps.pop(0)
                        else:
                            print("No previous steps available or the list is too short.")
                        for choice in lis:
                            main_logger.info(f"Step: {step} Choices: {lis}")
                            current_step = deepcopy(step)
                            current_step.append(choice)
                            steps_queue.append([current_step, prev_steps])
                    except Exception as e:
                        print(f"An error occurred: {e}")

                # codes = [""]
                higest_acc = 0
                best_code = ""
                # below code not tested with generated code yet
                for code in codes:
                    tokens = oj_interactions.submit_code_batch(code, prob.sample_test_cases, 'online')
                    total = 0
                    acc = 0
                    for token in tokens:
                        submission = oj_interactions.get_submission(token, 'online')
                        res = submission['status']["description"]
                        if "Accepted" in res:
                            acc += 1
                        total += 1
                    if acc/total > higest_acc:
                        higest_acc = acc/total
                        best_code = code
                
                main_logger.info(f"Best code: {best_code}, Accuracy: {higest_acc}")
                # TODO Work on the best code there

                # break since only wanted to test one of the prob instance as of now
                # Online Judge token might exceed limitation - requires 3^(num of stage) * 5 submissions per prob
                break


if __name__ == "__main__":
    main()