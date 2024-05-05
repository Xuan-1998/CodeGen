from sys import stdin

def solve():
    N = int(stdin.readline())
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(2, N + 1):
        for j in range(2, N + 1):
            num = i + j
            evens = sum(int(digit) for digit in str(num) if int(digit) % 2 == 0)
            odds = sum(int(digit) for digit in str(num) if int(digit) % 2 != 0)

            dp[i][j] = abs(evens - odds) + dp[max(0, i - 1)][max(0, j - 1)]

    return dp[N][N]

print(solve())
