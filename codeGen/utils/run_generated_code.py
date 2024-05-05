from oj_interactions import *
from problems import *
import json
import os
import pandas as pd
import subprocess
import time


def calculate_accuracy(expected_output, actual_output):
    return expected_output.count(actual_output) / len(expected_output)


def compare_outputs(py_file, json_file):
    with open(json_file) as f:
        test_cases = json.load(f)

    accuracy_rates = []
    expected_outputs = []
    actual_outputs = []

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["output"]
        expected_output = (
            [line.strip() for line in expected_output]
            if isinstance(expected_output, list)
            else expected_output.strip()
        )

        # Run the Python file and capture the output
        process = subprocess.Popen(
            ["python3", py_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        try:
            actual_output, _ = process.communicate(input=input_data.encode(), timeout=1)
            actual_output = actual_output.decode().strip()
        except Exception as e:
            process.terminate()
            print(f"An error occurred: {e}", py_file)
            actual_output = "INTERNAL ERROR OR TIMEOUT"

        # Calculate accuracy rate and add to the list
        expected_outputs.append(expected_output)
        actual_outputs.append(actual_output)
        accuracy = 1 if expected_output == actual_output else 0
        accuracy_rates.append(accuracy)

    if accuracy_rates:
        average_accuracy = sum(accuracy_rates) / len(accuracy_rates)
    else:
        average_accuracy = 0
    return average_accuracy, expected_outputs, actual_outputs, accuracy_rates


def get_acc_from_oj(py_file, json_file, method="online"):
    with open(json_file) as f:
        test_cases = json.load(f)

    accuracy_rates = []
    expected_outputs = []
    actual_outputs = []

    code = ""
    with open(py_file, "r") as f:
        code = f.read()
    tokens = submit_code_batch(code, test_cases, method=method)
    time.sleep(1)

    for token in tokens:
        result = get_submission(token, method=method)
        status, output = get_status_and_output(result)

        accuracy_rates.append(status)
        expected_output = result["expected_output"] if result and "expected_output" in result else "NO OUTPUT"
        expected_outputs.append(expected_output)
        actual_outputs.append(output)

    average_accuracy = sum("Accepted" in item for item in accuracy_rates) / len(
        accuracy_rates
    ) if accuracy_rates else 0
    return average_accuracy, expected_outputs, actual_outputs, accuracy_rates


def run_generated_code(
    root_dir: str = "results",
    model: str = "subprocess",  # "online" or "local" or 'subprocess'
):
    for method in os.listdir(root_dir):
        highest_accuracy = []
        if not os.path.isdir(os.path.join(root_dir, method)):
            continue

        for prob in os.listdir(os.path.join(root_dir, method)):
            if not os.path.isdir(os.path.join(root_dir, method, prob)):
                continue

            py_folder = os.path.join(root_dir, method, prob)
            py_files = [file for file in os.listdir(py_folder) if file.endswith(".py")]

            if (
                any(file.endswith(".csv") for file in os.listdir(py_folder))
                or len(py_files) == 0
            ):
                continue

            average_accuracies = []
            all_expected_outputs = []
            all_actual_outputs = []
            all_accuracy_rates = []

            json_file = os.path.join(py_folder, "test.json")
            for py_file in py_files:
                if model == "subprocess":
                    accuracy, expected_outputs, actual_outputs, accuracy_rates = (
                        compare_outputs(os.path.join(py_folder, py_file), json_file)
                    )
                else:
                    accuracy, expected_outputs, actual_outputs, accuracy_rates = (
                        get_acc_from_oj(
                            os.path.join(py_folder, py_file), json_file, method=model
                        )
                    )
                average_accuracies.append(accuracy)
                all_expected_outputs.append(expected_outputs)
                all_actual_outputs.append(actual_outputs)
                all_accuracy_rates.append(accuracy_rates)

            df = pd.DataFrame(
                {
                    "File": py_files,
                    "Average Accuracy": average_accuracies,
                    "Expected Output": all_expected_outputs,
                    "Actual Output": all_actual_outputs,
                    "Accuracy Rate": all_accuracy_rates,
                }
            )
            df.to_csv(f"{py_folder}/results.csv", index=False)
            highest_accuracy.append(max(average_accuracies))

        if highest_accuracy:
            print(
                f"{method}: Average Accuracy = {sum(highest_accuracy)}/{len(highest_accuracy)} = {sum(highest_accuracy)/len(highest_accuracy)}"
            )


def save_results_to_csv(
    py_folder: str,
    model: str = "subprocess",  # "online" or "local" or 'subprocess'
):
    py_files = [file for file in os.listdir(py_folder) if file.endswith(".py")]

    average_accuracies = []
    all_expected_outputs = []
    all_actual_outputs = []
    all_accuracy_rates = []

    json_file = os.path.join(py_folder, "test.json")
    for py_file in py_files:
        if model == "subprocess":
            accuracy, expected_outputs, actual_outputs, accuracy_rates = (
                compare_outputs(os.path.join(py_folder, py_file), json_file)
            )
        else:
            print(f"Running {os.path.join(py_folder, py_file)}, {len(average_accuracies)}/{len(py_files)}")
            accuracy, expected_outputs, actual_outputs, accuracy_rates = (
                get_acc_from_oj(
                    os.path.join(py_folder, py_file), json_file, method=model
                )
            )
        average_accuracies.append(accuracy)
        all_expected_outputs.append(expected_outputs)
        all_actual_outputs.append(actual_outputs)
        all_accuracy_rates.append(accuracy_rates)

    df = pd.DataFrame(
        {
            "File": py_files,
            "Average Accuracy": average_accuracies,
            "Expected Output": all_expected_outputs,
            "Actual Output": all_actual_outputs,
            "Accuracy Rate": all_accuracy_rates,
        }
    )
    df.to_csv(f"{py_folder}/results.csv", index=False)
    return average_accuracies


def compare_with_baseline(
    method: str = "tree_search_llama",
    baseline: str = "zero_shot",
    root_dir: str = "results",
    model: str = "subprocess",  # "online" or "local" or 'subprocess'
):
    highest_accuracy = []
    baseline_high_accuracy = []

    for prob in os.listdir(os.path.join(root_dir, method)):
        if not os.path.isdir(os.path.join(root_dir, method, prob)):
            continue

        py_folder = os.path.join(root_dir, method, prob)
        py_files = [file for file in os.listdir(py_folder) if file.endswith(".py")]
        if (
            any(file.endswith(".csv") for file in os.listdir(py_folder))
            or len(py_files) == 0
        ):
            print(f"Skipping {py_folder}")
            continue
        average_accuracies = save_results_to_csv(py_folder, model)

        baseline_py_folder = os.path.join(root_dir, baseline, prob)
        if not os.path.isdir(baseline_py_folder):
            baseline_average_accuracies = [0 for _ in range(len(py_files))]
            print(f"Baseline not found for {py_folder}")
        else:
            baseline_average_accuracies = save_results_to_csv(baseline_py_folder, model)

        highest_accuracy.append(max(average_accuracies))
        baseline_high_accuracy.append(max(baseline_average_accuracies))

    if highest_accuracy:
        print(
            f"{method}: Average Accuracy = {sum(highest_accuracy)}/{len(highest_accuracy)} = {sum(highest_accuracy)/len(highest_accuracy)}"
        )
    if baseline_high_accuracy:
        print(
            f"{baseline}: Average Accuracy = {sum(baseline_high_accuracy)}/{len(baseline_high_accuracy)} = {sum(baseline_high_accuracy)/len(baseline_high_accuracy)}"
        )


def analyze_csv_with_difficulty(
    method: str = "tree_search_llama",
    baseline: str = "zero_shot",
    root_dir: str = "results",
):
    model_accuracies = []
    baseline_accuracies = []
    for prob in os.listdir(os.path.join(root_dir, method)):
        if not os.path.isdir(os.path.join(root_dir, method, prob)):
            continue

        py_folder = os.path.join(root_dir, method, prob)
        csv_file = os.path.join(py_folder, "results.csv")
        df = pd.read_csv(csv_file)
        highest_accuracy = df["Average Accuracy"].max()
        sample_budget = len(df["Average Accuracy"])

        baseline_py_folder = os.path.join(root_dir, baseline, prob)
        baseline_csv_file = os.path.join(baseline_py_folder, "results.csv")
        if not os.path.isfile(baseline_csv_file):
            print(f"Baseline not found for {py_folder}")
            baseline_high_accuracy = 0
        else:
            baseline_df = pd.read_csv(baseline_csv_file)
            baseline_high_accuracy = baseline_df["Average Accuracy"][:max(sample_budget, 75)].max()

        prob_file = os.path.join(py_folder, "prob.json")
        with open(prob_file) as f:
            prob_str = f.read()
            import codecs
            unescaped_str = codecs.decode(prob_str, 'unicode_escape')

        prob_json = Problem.from_json(unescaped_str[1:-1])

        print(
            f"Problem: {prob}, Difficulty: {prob_json.difficulties}, Highest Accuracy: {highest_accuracy:.2f}, Sample Budget: {sample_budget}, Baseline Accuracy: {baseline_high_accuracy:.2f}"
        )
        model_accuracies.append(highest_accuracy)
        baseline_accuracies.append(baseline_high_accuracy)

    if model_accuracies and baseline_accuracies:
        print(
            f"{method}: Average Accuracy = {sum(model_accuracies)}/{len(model_accuracies)} = {sum(model_accuracies)/len(model_accuracies)}"
        )
        print(
            f"{baseline}: Average Accuracy = {sum(baseline_accuracies)}/{len(baseline_accuracies)} = {sum(baseline_accuracies)/len(baseline_accuracies)}"
        )


if __name__ == "__main__":
    # run_generated_code(model='online')
    # run_generated_code()
    # compare_with_baseline('tree_search_4_medium_hard', 'zero_shot')
    analyze_csv_with_difficulty('tree_search_4_medium_hard')
