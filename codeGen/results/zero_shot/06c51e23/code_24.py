import sys

n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
fraction = float(sys.stdin.readline())

grade = 0

while t > 0 and n > 0:
    if fraction >= 1.5:
        grade += 1
        fraction -= 1
    else:
        break
    n -= 1
    t -= 1

print(grade)
