import sys

n = int(sys.stdin.readline())
marks = list(map(int, sys.stdin.readline().split()))

total_marks = sum(range(1, n+1))
min_sum = total_marks

for i in range(n):
    total_marks -= (i + 1) - marks[i]
    min_sum = min(min_sum, total_marks)

print(min_sum)
