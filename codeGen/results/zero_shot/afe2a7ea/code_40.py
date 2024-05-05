# Example inputs and expected outputs
example_inputs = [1, 2, 3]
expected_outputs = [7, 14, 28]

for input, output in zip(example_inputs, expected_outputs):
    print(f"Input: {input}, Expected Output: {output}")
    result = calculate_probability(input)
    if result == output:
        print("Correct!")
    else:
        print(f"Incorrect! Expected {output}, got {result}")
