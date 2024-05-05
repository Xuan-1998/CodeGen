import sys

n = int(input())
marks = list(map(int, input().split()))

marks.sort(reverse=True)

total_sum = 0
max_mark = 0

for i in range(n):
    max_mark += marks[i]
    total_sum += max_mark - sum(marks[:i+1])

print(total_sum)
