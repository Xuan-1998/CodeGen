def solution():
    a, b = map(int, input().split())
    
    dp = [[0] * (b.bit_length() + 1) for _ in range(a.bit_length() + 1)]

    for j in range(b.bit_length() + 1):
        dp[0][j] = ((1 << j) - 1) & b

    for i in range(1, a.bit_length() + 1):
        for j in range(b.bit_length() + 1):
            if i > 0:
                dp[i][j] = (dp[i-1][j] + (a >> (i-1)) ^ ((1 << j) - 1) & b) % (10**9 + 7)
            else:
                dp[i][j] = ((1 << j) - 1) & b

    total_sum = sum(dp[-1])
    print(total_sum)

solution()
