def find_special_numbers(a, b):
    special_numbers = []
    
    # Iterate through each number in the given range
    for num in range(a, b+1):
        digit_sum = 0
        
        # Convert the number to a string and iterate through each character (digit)
        for i, digit in enumerate(str(num)):
            digit_sum += int(digit) ** (i + 1)
        
        # Check if the sum of digits raised to their positions is equal to the original number
        if num == digit_sum:
            special_numbers.append(num)
    
    return sorted(special_numbers)

# Example usage:
a, b = map(int, input().split())
print(" ".join(map(str, find_special_numbers(a, b))))
