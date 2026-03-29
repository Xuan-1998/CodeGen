import sys

def min_cost_to_sort_strings():
    n = int(sys.stdin.readline().strip())
    costs = list(map(int, sys.stdin.readline().strip().split()))
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    dp = [0] * (n + 1)
    for i in range(1, n):
        if strings[i-1] <= strings[i]:
            dp[i] = dp[i-1]
        else:
            for j in range(i):
                if strings[j] > strings[i]:
                    dp[i] = min(dp[i], dp[j] + costs[i])
                    break

    return sum(dp) if dp[-1] != 0 else -1
