import sys

def solve():
    a = int(input())
    b = int(input())

    dp = [[0] * (314160) for _ in range(20)]
    for i in range(1, 20):
        dp[i][0] = 0
        for j in range(b):
            dp[i][j+1] = (dp[i-1][j] ^ ((b << i) & (a >> (9-i)))) % (10**9 + 7)

    result = 0
    for i in range(20):
        result += dp[i][314159]
    return result

print(solve())
