import sys

# Read input from stdin
n, t = map(int, sys.stdin.readline().split())
frac = float(sys.stdin.readline())

# Initialize maximum grade to 0
max_grade = 0

# Iterate through all possible rounding positions
for i in range(1, n):
    # Calculate the rounded fraction at this position
    rounded_frac = round(frac, i)
    
    # Calculate the resulting grade for this rounded fraction
    grade = int(rounded_frac * 100)
    
    # Update maximum grade if this rounded fraction yields a higher grade
    max_grade = max(max_grade, grade)

print(max_grade)
