import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
decimal_fraction = float(sys.stdin.readline())

grade = 0
for i in range(n):
    if t >= 1:
        grade += 10 ** (n - 1 - i)
        t -= 1
    else:
        break

print(int(grade))
