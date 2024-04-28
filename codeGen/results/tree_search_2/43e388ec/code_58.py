def solve():
    a, b = map(int, input().split())
    dp = [[0] * 20 for _ in range(21)]
    mod = int(1e9) + 7

    for i in range(b+1):
        left_shifted_b = (b << i) % mod
        dp[i][0] = (a ^ left_shifted_b) % mod

    for j in range(1, 20):
        for i in range(j+1):
            next_state = (i - 1, (j-1)%20)
            if next_state[0] >= 0:
                dp[next_state[0]][next_state[1]] = (dp[i][j-1] + a ^ ((b << j) % mod)) % mod

    result = 0
    for i in range(314159+1):
        result = (result + dp[i][19]) % mod

    print(result)
