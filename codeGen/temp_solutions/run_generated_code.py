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

        # Run the Python file and capture the output
        process = subprocess.Popen(["python", py_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            actual_output, _ = process.communicate(input=input_data.encode())
            actual_output = actual_output.decode().strip()
        except Exception as e:
            print(f"An error occurred: {e}", py_file)
            actual_output = ""

        # Calculate accuracy rate and add to the list
        # print(f"Expected: {expected_output}")
        expected_outputs.append(expected_output)
        # print(f"Actual: {actual_output}")
        actual_outputs.append(actual_output)
        accuracy = calculate_accuracy(expected_output, actual_output)
        accuracy_rates.append(accuracy)

    # Calculate the average accuracy rate for the file
    average_accuracy = sum(accuracy_rates) / len(accuracy_rates)

    return average_accuracy, expected_outputs, actual_outputs, accuracy_rates

def main():
    root_dir = r"../results"
    for folder in os.listdir(root_dir):
        if not os.path.isdir(os.path.join(root_dir, folder)):
            continue
        py_folder = os.path.join(root_dir, folder)
        py_files = [file for file in os.listdir(py_folder) if file.endswith(".py")]
        average_accuracies = []
        all_expected_outputs = []
        all_actual_outputs = []
        all_accuracy_rates = []

        json_file = os.path.join(py_folder, "test.json")
        for py_file in py_files:
            accuracy, expected_outputs, actual_outputs, accuracy_rates = compare_outputs(os.path.join(py_folder, py_file), json_file)
            print(f"{py_file}: Accuracy = {accuracy}")
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

if __name__ == "__main__":
    main()
