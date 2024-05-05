import math

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bad_primes = set(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i] = a[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            gcd = a[j]
            for k in range(i, j):
                gcd = math.gcd(gcd, a[k])
            if gcd in bad_primes:
                dp[i][j] = 0
            else:
                prev_beauty = dp[i][j - 1]
                new_beauty = prev_beauty + (a[j] if gcd > 1 else -a[j])
                dp[i][j] = max(prev_beauty, new_beauty)

    print(dp[0][n - 1])

if __name__ == "__main__":
    solve()
