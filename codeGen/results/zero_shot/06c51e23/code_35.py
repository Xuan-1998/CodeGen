import sys

# Read input
n, t = map(int, sys.stdin.readline().split())
fraction = float(sys.stdin.readline())

# Initialize maximum grade
max_grade = int(fraction)

# Check each digit after decimal point
for i in range(1, n):
    # Calculate the new grade with current digit rounded
    new_grade = max_grade + (0 if int((fraction * 10) % 10) >= 5 else -1)
    
    # Check if time limit is exceeded
    if t <= 0:
        break
    
    # Update maximum grade and time left
    max_grade = new_grade
    t -= 1

# Print the maximum possible grade
print(max_grade)
