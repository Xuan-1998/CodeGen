import sys

# Read inputs from stdin
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = float(sys.stdin.readline())

# Initialize maximum possible grade
max_grade = 0

# Iterate through each digit after the decimal point
for i in range(1, n):
    # Calculate the current grade for this rounding scenario
    current_grade = (int(fraction * 10**i) + 4) // 5
    
    # Update the maximum possible grade if necessary
    max_grade = max(max_grade, current_grade)

# Print the maximum possible grade
print(max_grade)

