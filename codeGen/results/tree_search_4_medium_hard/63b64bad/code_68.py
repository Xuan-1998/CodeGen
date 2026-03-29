code block
n = int(input())
sequence = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    while sequence[i] > 0 and i <= n:
        dp[i] += sequence[i]
        i += sequence[i]

print(dp[1])
