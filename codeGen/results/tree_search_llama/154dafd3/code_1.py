def round_to_nearest_multiple_of_five(numbers):
    return [round(num / 5) * 5 for num in numbers]

# Test the function
numbers = [float(x.strip()) for x in input().split(',')]
print(*round_to_nearest_multiple_of_five(numbers), sep='\n')
