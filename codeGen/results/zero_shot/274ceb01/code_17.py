import sys

n = int(input())
marks = list(map(int, input().split()))
prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + marks[i-1]

min_sum = float('inf')
for i in range(1, n+1):
    min_sum = min(min_sum, prefix_sum[i] - i)

print(min_sum)
