import sys
from math import ceil, floor

# Read input from stdin
numbers = [float(x) for x in sys.stdin.readline().split()]

# Round each number to the nearest multiple of 5
rounded_numbers = []
for num in numbers:
    if num % 5 <= 0.5:  # if the number is closer to the previous multiple of 5
        rounded_numbers.append(floor(num / 5) * 5)
    else:  # if the number is closer to the next multiple of 5
        rounded_numbers.append(ceil(num / 5) * 5)

# Print the output to stdout
print(' '.join(map(str, rounded_numbers)))
