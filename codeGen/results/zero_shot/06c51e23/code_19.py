import sys

# Read input from stdin
n = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())
frac = float(sys.stdin.readline().strip())

max_grade = 0
for i in range(n):
    if t > 0:  # Check if time limit is still available
        if (int((10**i) * frac)) % 10 >= 5:  # If the fractional part is greater than or equal to 0.5, round up
            max_grade = int(100 + (10**n) * frac)
            break
        else:
            t -= 1  # Consume time for rounding down
    else:
        break

print(max_grade)
