import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

longest_lengths = set(dp)
max_length = max(longest_lengths)
num_longest = len([x for x in dp if x == max_length])

print(num_longest)
