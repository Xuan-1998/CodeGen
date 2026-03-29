import sys

n = int(input())
marks = list(map(int, input().split()))

min_sum = float('inf')
for i in range(1, n+1):
    below_water = n - marks[i-1]
    min_sum = min(min_sum, below_water)

print(min_sum)
