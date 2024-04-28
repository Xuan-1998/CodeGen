def solve():
    # Read input from stdin
    a = int(input())
    b = int(input())

    k = len(bin(a)) - 2  # number of bits in a

    # Initialize dynamic programming table
    dp = [[0] * (k + 1) for _ in range(k + 1)]

    # Fill up the table using bottom-up approach with tabulation
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if i == 0 or j == 0:
                dp[i][j] = a % (10**9 + 7) if i == 0 else b % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j-1]
                for bit in range(i):
                    if (a >> bit) & 1 and (b >> j - 1) & 1:
                        dp[i][j] += (2 ** (k - i)) % (10**9 + 7)
                        break

    # Compute the final answer using the table
    ans = sum((dp[i][k] if i == k else 0) for i in range(k + 1))
    print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
