import sys

def solve():
    n = int(input())
    times = list(map(int, input().split()))
    healths = list(map(int, input().split()))

    dp = [0] * (max(times) + 1)
    for i in range(n):
        dp[times[i]] = max(dp[times[i]], dp[healths[i] - 1]) if healths[i] > 1 else 0

    for i in range(1, len(dp)):
        dp[i] = min(dp[i], dp[i-1] + (i - 1)) if i > times[-1] - times[0] else dp[i]

    print(max(dp))

if __name__ == "__main__":
    solve()
