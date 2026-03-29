import sys

def solve():
    n, m = map(int, input().split())
    k = int(input())
    primes = list(map(int, input().split()))

    # Calculate the product of prime factors
    prod = 1
    for p in primes:
        prod *= p

    # Initialize dynamic programming table
    dp = [[0] * (n - 1) for _ in range(n)]

    # Fill up dynamic programming table
    for i in range(1, n):
        parent_i = int(input()) - 1
        for j in range(n - 1):
            if j < i:
                dp[i][j] = dp[parent_i][j]
            else:
                dp[i][j] = max(dp[parent_i][j], dp[i][j-1])
            if j > 0 and dp[i][j] > 1:
                dp[i][j] -= 1

    # Calculate the maximum possible distribution index
    dist_index = sum(sum(range(1, n)) for i in range(n - 1) for j in range(i + 1, n))

    print(dist_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
