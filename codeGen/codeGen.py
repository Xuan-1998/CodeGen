from utils import *
from dataset import *
import os

main_logger = codeGen_logger.setup_logging()

def main():
    main_logger.info("codeGen starts")
    # initialize_problems(100, "Dynamic Programming")
    data_path = r"../data"
    for source in os.listdir(data_path):
        probs_path = os.path.join(data_path, source, "problems.jsonl")
        with open(probs_path, 'r') as file:
            for line in file:
                prob = problems.Problem.from_jsonl(line)
                main_logger.info(f"Processing problem {source} {prob.url}")
                lis, response = coding.provide_algorithm_coder(prob.statement, "Dynamic Programming")
                main_logger.info(f"Algorithm: {lis}")
                break


if __name__ == "__main__":
    main()