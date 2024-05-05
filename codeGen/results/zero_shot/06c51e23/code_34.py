import sys

# Read input from standard input
n, t = map(int, sys.stdin.readline().split())
frac_str = sys.stdin.readline()

# Convert decimal fraction to float
frac = float(frac_str)

# Initialize maximum grade and current time
max_grade = 0
cur_time = 0

# Iterate over each digit after the decimal point
for i in range(1, n+1):
    # Calculate new grade for rounding up or down
    round_up_grade = int((frac * (10**i)) + 0.5)
    round_down_grade = int(frac * (10**i))
    
    # Update maximum grade and current time accordingly
    max_grade = max(max_grade, round_up_grade)
    cur_time += i
    
    if cur_time > t:
        break

print(max_grade)
