import sys
import heapq

n = int(sys.stdin.readline())
marks_above_water = list(map(int, sys.stdin.readline().split()))

cumulative_sum = [0] * (n + 1)
for i, mark in enumerate(marks_above_water):
    cumulative_sum[i+1] = cumulative_sum[i] + mark

marks_below_water = [cumulative_sum[i] - cumulative_sum[i-1] for i in range(1, n+1)]

min_sum = 0
for i in range(n):
    min_sum += heapq.heappop(marks_below_water)

print(min_sum)
