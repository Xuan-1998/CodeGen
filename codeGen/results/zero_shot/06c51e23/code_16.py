import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = sys.stdin.readline().strip()

grade = 0
for i in range(n):
    if t > 1 and fraction[i] != '.':
        if grade < (int(fraction[i+1]) * 10 + 5) / 2:
            grade = (int(fraction[i+1]) * 10 + 5) / 2
        t -= 1
    else:
        break

print(grade)
