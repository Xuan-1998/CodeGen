def solution():
    a, b = map(int, input().split())
    dp = [[0] * (31 + 1) for _ in range(31 + 1)]

    # Base case: DP[0] = a ^ b
    for i in range(a.bit_length()):
        dp[i][0] = ((b >> i) & 1) ^ a

    for i in range(1, 31 + 1):
        for j in range(i + 1):
            # Update state: DP[i][j] = (DP[i-1][j] ^ (b >> i%31)) % (10**9 + 7)
            dp[i][j] = ((dp[i-1][j] if i > 0 else a) ^
                        ((b >> i%31) & 1)) % (10**9 + 7)

    # Calculate the sum of OR(a, b << i) for all values of i
    total_sum = 0
    for j in range(31 + 1):
        total_sum += dp[314159][j]
    return total_sum

print(solution())
