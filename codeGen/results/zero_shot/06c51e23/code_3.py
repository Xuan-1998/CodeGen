import sys

n = int(input())
frac = float(input())

grade = 0
time_taken = 0

for i in range(1, n + 1):
    if time_taken + len(str(i)) <= t:
        grade += i
        time_taken += len(str(i))
    else:
        break

print(int(grade * (10 ** n)))
