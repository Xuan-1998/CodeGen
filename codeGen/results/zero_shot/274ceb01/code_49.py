n = int(input())  # number of days
marks = list(map(int, input().split()))  # marks strictly above the water on each day

# calculate prefix sum array
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + (marks[i-1] - marks[i])

# find minimum sum
min_sum = float('inf')
for i in range(1, n):
    min_sum = min(min_sum, prefix_sum[i] - prefix_sum[i-1])

print(min_sum)
