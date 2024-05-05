code
N, M, C = map(int, input().split())
U = list(map(int, input().split()))
L = list(map(int, input().split()))

dp = [0] * (C + 1)
for i in range(C + 1):
    dp[i] = (dp[i - 1] if i > 0 else 1) + sum(1 for j in U if j == i) * (dp[i - 1] if i > 0 else 1)

print(*map(str, dp), sep=' ')
!!!
