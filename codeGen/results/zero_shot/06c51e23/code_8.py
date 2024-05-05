python
import sys

# Read input from stdin
n, t = map(int, sys.stdin.readline().split())
fraction = float(sys.stdin.readline())

# Initialize maximum grade as 0.00
max_grade = 0.00

# Iterate over each digit after decimal point
for i in range(n):
    # Calculate the grade for this rounding choice
    grade = round(fraction, i+1)
    
    # Check if time limit is exceeded
    if (len(str(grade)) - str(grade).index('.')) > t:
        break
    
    # Update maximum grade if possible
    max_grade = max(max_grade, grade)

# Print the maximum grade to stdout
print("{:.2f}".format(max_grade))
