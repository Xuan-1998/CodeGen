import sys

def max_earnings(k, n, m, p):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if p[j] > dp[i - 1]:
                dp[i] = max(dp[i], p[j])
            else:
                dp[i] += p[j]
    return dp[n]

def solve():
    n, k, m, p = [int(x) for x in input().split()]
    earnings = max_earnings(k, n, m, p)
    print(*[f"{i+1} {j+1}" for i, j in zip(range(n), p)], sep='\n')

if __name__ == "__main__":
    solve()
