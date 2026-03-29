from collections import defaultdict

def solve_dp(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        x, y = 1, 0
        cycle_length = 0
        seen = set()
        while True:
            if (x, y) in seen:
                break
            seen.add((x, y))
            x += a[i]
            y += a[i]
            x -= a[x]
            y += a[x]
            cycle_length += 1
        dp[i] = y % (10**9 + 7)
    return [dp[i] for i in range(2, n + 1)]

n = int(input())
a = list(map(int, input().split()))
print(*solve_dp(n), sep='\n')
