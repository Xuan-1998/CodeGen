import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = float(sys.stdin.readline())

max_grade = 0
for i in range(n):
    if (10 ** (i + 1)) * fraction >= t:
        max_grade += 5
    else:
        remain = (10 ** i) * fraction % 10
        if remain >= 5:
            max_grade += 6 - (10 - remain)
        break

print(max_grade)
