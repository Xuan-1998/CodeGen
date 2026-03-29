import sys
input = sys.stdin.readline

def solve(n, m):
    dp = [0] * (len(str(n)) + 1)
    for i in range(1, len(dp)):
        dp[i] = min((dp[i-1] + 1) % (10**9+7), i)
    return dp[-1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
