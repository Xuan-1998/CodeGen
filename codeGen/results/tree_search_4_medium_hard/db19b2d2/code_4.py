import sys

def probability():
    n, m, h = map(int, input().split())
    S = list(map(int, input().split()))

    if sum(S) < n:
        return -1.0  # not enough players to form a team

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = sum(dp[j] for j in range(h - 1, min(i, h) + 1))
    probability = sum(S) >= n
    dp[-1] += probability

    return [x / (n * len(S)) for x in dp][n]

print(probability())
