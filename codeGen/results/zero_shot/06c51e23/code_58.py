import sys

n = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())
fraction = float(sys.stdin.readline().strip())

grade = 0
for i in range(n - 1):
    if (i + 1) * t < (n - i - 1) * 10:  # Check if rounding would exceed time limit
        break
    else:
        grade += int((fraction * 10**i) // 10**i)

print(grade)
