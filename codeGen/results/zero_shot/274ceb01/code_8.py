import sys

n = int(sys.stdin.readline())
marks_per_day = list(map(int, sys.stdin.readline().split()))

min_sum = sum(marks_per_day)
for i in range(1, n+1):
    min_sum += (i - 1) * marks_per_day[i-1] // i

print(min_sum)
