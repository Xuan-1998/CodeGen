def count_bitwise_AND_more_than_or_equal_to_k XOR_less_than_j(k, n):
    MOD = 10**9 + 7
    dp = [[[0] * (k + 1) for _ in range(j + 1)] for _ in range(n + 1)]

    # Base case: empty array
    dp[0][j][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            for x in range(2**k):
                if all((x & y) >= k - 1 for y in range(i)):
                    dp[i][j][x] += sum(dp[i-1][max(0, (x & y))][y] for y in range(k))
                else:
                    dp[i][j][x] = 1 if all((x ^ y) < k - 1 for y in range(i)) else 0
                dp[i][j][x] %= MOD

    return sum(dp[n][0])

# Read input from stdin and print the answer to stdout
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_bitwise_AND_more_than_or_equal_to_k(k, n))
