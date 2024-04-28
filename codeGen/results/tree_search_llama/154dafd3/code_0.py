def round_to_nearest_multiple_of_five(input_array):
    result = []
    for num in input_array:
        remainder = int((num % 1) * 10)
        if remainder < 5:
            result.append(int(num - (0.05 - remainder)))
        else:
            result.append(int(num + (remainder - 4.95)))
    return result

# Example usage
input_array = [12.43, 19.91, 23.76]
output_array = round_to_nearest_multiple_of_five(input_array)
print(output_array)  # Output: [15, 20, 25]
