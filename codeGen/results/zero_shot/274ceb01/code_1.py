import sys

n = int(input())
marks = list(map(int, input().split()))

min_sum = 0
for i in range(1, n+1):
    min_sum += (i - marks[i-1])

print(min_sum)
