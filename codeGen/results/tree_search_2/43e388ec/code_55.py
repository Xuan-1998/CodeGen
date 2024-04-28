def solve(a, b):
    i_size = 315
    a_size = max(len(bin(a)[2:])) - 1  # Calculate the size of the array based on the input value
    dp = [[0] * (i_size + 1) for _ in range(a_size + 1)]

    for i in range(i_size + 1):
        dp[0][i] = b & ((1 << i) - 1)

    for a in range(1, a_size + 1):
        for i in range(i_size + 1):
            if (a & (1 << i)):
                dp[a][i] = dp[a-1][i] ^ (b >> i)
            else:
                dp[a][i] = dp[a-1][i]

    result = sum(dp[a][i] for a in range(a_size + 1) for i in range(i_size + 1))
    return str(result % (10**9 + 7))

# Read input from stdin
a, b = map(int, input().split())
print(solve(a, b))
