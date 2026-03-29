import sys
input = sys.stdin.read().split()
arr = [int(x) for x in input[0].split()]
n = len(arr)
dp = [[False] * n for _ in range(n)]
max_length = 0

for i in range(n):
    for j in range(i, n):
        if arr[j] > arr[i]:
            dp[i][j] = True
            max_length = max(max_length, j - i + 1)

count = sum(1 for row in dp[-1:] if any(row))

print(count)
