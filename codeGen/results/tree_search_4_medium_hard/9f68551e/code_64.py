import sys

def solve():
    n = int(sys.stdin.readline())
    times = list(map(int, sys.stdin.readline().split()))
    healths = list(map(int, sys.stdin.readline().split()))

    dp = [0] * (n + 1)
    max_damage = 0

    for i in range(n):
        if times[i] > max_damage:
            dp[i + 1] = min(dp[i] + 1, healths[i])
        else:
            dp[i + 1] = min(dp[i] + times[i] - max_damage, healths[i])

        max_damage = max(max_damage, times[i])

    return dp[-1]

print(solve())
