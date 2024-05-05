n = int(input())
sequence = list(map(int, input().split()))
dp = [-1] * (n + 1)

def recursive_dp(y, x):
    if x <= 0 or x > n:
        return -1
    x += sequence[x - 2]
    y += sequence[x - 2]
    x -= sequence[x - 2]
    y += sequence[x - 2]
    return max(recursive_dp(y, x + 1), recursive_dp(y + sequence[x], x - sequence[x]))

for i in range(2, n + 1):
    dp[i] = recursive_dp(0, i)
print(dp[-1])
