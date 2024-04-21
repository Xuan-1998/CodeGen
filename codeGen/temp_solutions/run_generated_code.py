import os
import json
import subprocess

py_folder = "to_verify"
json_folder = "to_verify"

def calculate_accuracy(expected_output, actual_output):
    return expected_output.count(actual_output) / len(expected_output)

def compare_outputs(py_file, json_file):
    with open(json_file) as f:
        test_cases = json.load(f)["sample_test_cases"]

    accuracy_rates = []
    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["output"]

        # Run the Python file and capture the output
        process = subprocess.Popen(["python", py_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        actual_output, _ = process.communicate(input=input_data.encode())
        actual_output = actual_output.decode().strip()

        # Calculate accuracy rate and add to the list
        print(f"Expected: {expected_output}")
        print(f"Actual: {actual_output}")
        accuracy = calculate_accuracy(expected_output, actual_output)
        accuracy_rates.append(accuracy)

    # Calculate the average accuracy rate for the file
    average_accuracy = sum(accuracy_rates) / len(accuracy_rates)

    return average_accuracy

def main():
    py_files = [file for file in os.listdir(py_folder) if file.endswith(".py")]
    json_files = [file for file in os.listdir(json_folder) if file.endswith(".json")]

    for py_file in py_files:
        json_file = os.path.join(json_folder, py_file.replace(".py", ".json"))

        # Compare outputs and get accuracy rate
        accuracy = compare_outputs(os.path.join(py_folder, py_file), json_file)

        print(f"{py_file}: Accuracy = {accuracy}")

if __name__ == "__main__":
    main()
