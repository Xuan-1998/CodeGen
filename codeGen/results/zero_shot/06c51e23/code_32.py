import sys

def max_grade(n, t, frac):
    # Initialize the maximum grade and the current time
    max_grade = 0
    curr_time = 0
    
    # Iterate over each digit after the decimal point
    for i in range(1, n+1):
        # Calculate the value of rounding at this place
        rounded_value = round(float(frac[:i+1]), 2)
        
        # Update the maximum grade and current time accordingly
        max_grade = max(max_grade, int(rounded_value))
        curr_time += i
        
        # If we've exceeded the time limit, break out of the loop
        if curr_time > t:
            break
    
    return max_grade

# Read input from stdin
n, t = map(int, sys.stdin.readline().split())
frac = float(sys.stdin.readline())

# Calculate and print the maximum grade
max_grade = max_grade(n, t, frac)
print(max_grade)
