import sys

def solve():
    n = int(input())
    parent = list(map(int, input().split()))
    ranges = []
    for _ in range(n):
        l, r = map(int, input().split())
        ranges.append((l, r))

    dp = [[[0] * (10**9 + 1) for _ in range(2*10**5+1)] for _ in range(2*10**5+1)]

    for i in range(n-1):
        j = parent[i]
        for k in range(min(ranges[j][1], ranges[i][1]) - max(ranges[j][0], ranges[i][0]) + 1):
            dp[j][i][k] = min(dp[j][i][k], dp[j][j][k] + 1)

    return sum(dp[0][i][0] for i in range(1, n))

print(solve())
