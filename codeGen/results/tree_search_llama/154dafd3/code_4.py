def round_to_nearest_multiple_of_5(numbers):
    result = []
    for num in numbers:
        # Convert to scientific notation with exponent as an integer
        sci_notation = "{:.2e}".format(num)
        # Split the scientific notation into coefficient and exponent
        coeff, exp = sci_notation.split("e")
        # Adjust the exponent to round the number to its nearest multiple of 5
        exp = str(int(float(exp)) // 1 + (round(float(exp)) % 1 > 0.5))
        # Reconstruct the scientific notation with the adjusted exponent
        rounded_sci_notation = "{}e{}".format(coeff, exp)
        # Convert back to decimal form and add to result
        result.append(float(rounded_sci_notation))
    return result

input_numbers = list(map(float, input().split(",")))
rounded_numbers = round_to_nearest_multiple_of_5(input_numbers)
print(", ".join(map(str, rounded_numbers)))
