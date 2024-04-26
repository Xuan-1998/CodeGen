import os
import json
import subprocess
import pandas as pd

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
        expected_output = [line.strip() for line in expected_output] if isinstance(expected_output, list) else expected_output.strip()

        # Run the Python file and capture the output
        process = subprocess.Popen(["python", py_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            actual_output, _ = process.communicate(input=input_data.encode(), timeout=1)
            actual_output = actual_output.decode().strip()
        except Exception as e:
            print(f"An error occurred: {e}", py_file)
            actual_output = "INTERNAL ERROR OR TIMEOUT"

        # Calculate accuracy rate and add to the list
        expected_outputs.append(expected_output)
        actual_outputs.append(actual_output)
        accuracy = 1 if expected_output == actual_output else 0
        accuracy_rates.append(accuracy)

    average_accuracy = sum(accuracy_rates) / len(accuracy_rates)
    return average_accuracy, expected_outputs, actual_outputs, accuracy_rates

def run_generated_code(
        root_dir: str = "results",
        model: str = "subprocess" # "online" or "local" or 'subprocess'
):
    # root_dir = r"results"
    for method in os.listdir(root_dir):
        highest_accuracy = []
        if not os.path.isdir(os.path.join(root_dir, method)):
            continue

        for prob in os.listdir(os.path.join(root_dir, method)):
            if not os.path.isdir(os.path.join(root_dir, method, prob)):
                continue

            py_folder = os.path.join(root_dir, method, prob)
            py_files = [file for file in os.listdir(py_folder) if file.endswith(".py")]

            if any(file.endswith(".csv") for file in os.listdir(py_folder)) or len(py_files) == 0:
                continue

            average_accuracies = []
            all_expected_outputs = []
            all_actual_outputs = []
            all_accuracy_rates = []

            json_file = os.path.join(py_folder, "test.json")
            for py_file in py_files:
                accuracy, expected_outputs, actual_outputs, accuracy_rates = compare_outputs(os.path.join(py_folder, py_file), json_file)
                # print(f"{prob}{py_file}: Accuracy = {accuracy}")
                average_accuracies.append(accuracy)
                all_expected_outputs.append(expected_outputs)
                all_actual_outputs.append(actual_outputs)
                all_accuracy_rates.append(accuracy_rates)

            df = pd.DataFrame({
                "File": py_files,
                "Average Accuracy": average_accuracies,
                "Expected Output": all_expected_outputs,
                "Actual Output": all_actual_outputs,
                "Accuracy Rate": all_accuracy_rates
            })
            df.to_csv(f"{py_folder}/results.csv", index=False)
            highest_accuracy.append(max(average_accuracies))
        
        if highest_accuracy:
            print(f"{method}: Average Accuracy = {sum(highest_accuracy)}/{len(highest_accuracy)} = {sum(highest_accuracy)/len(highest_accuracy)}")

if __name__ == "__main__":
    run_generated_code()
