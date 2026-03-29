import sys

# Input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

# Initialize dp array with size n+1 and fill it up from left to right
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = sys.maxsize

for i in range(1, n + 1):
    for j in range(i):
        if strings[j] <= strings[i - 1]:
            dp[i] = min(dp[i], dp[j] + costs[i - 1])
        elif strings[j] >= strings[0]:
            dp[i] = min(dp[i], dp[0] + (i - 1) * costs[i - 1])

# Print the minimum total cost required to sort the strings in lexicographical order
print(dp[-1]) if dp[-1] != sys.maxsize else print(-1)
