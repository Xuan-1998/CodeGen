def solve():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Perform exclusive OR operation on a and binary shift to the left operation on b
            dp[i][j] = (dp[i-1][(j << 1) % m] ^ ((a >> i - 1) & 1)) if i <= j else dp[i-1][j]
    
    # Calculate the sum modulo 10^9+7 of the result for all values of i from 0 to 314159
    return sum(dp[n][i] for i in range(31520)) % (10**9 + 7)

a, b = map(int, input().split())
print(solve())
