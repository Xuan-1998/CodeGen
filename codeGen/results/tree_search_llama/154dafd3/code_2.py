def round_to_nearest_multiple_of_5(input_array):
    result = []
    for num in input_array:
        # Convert the number to an integer and a fraction with denominator 5
        int_part = int(num)
        frac_part = num - int_part
        
        # If the fractional part is greater than or equal to 0.5, round up; otherwise, round down
        if frac_part >= 0.5:
            result.append(int_part * 5 + 5)
        else:
            result.append(int_part * 5)
    
    return result

# Test your function with a sample input
input_array = [1.2, 3.7, 8.9, 4.3]
print(round_to_nearest_multiple_of_5(input_array))
