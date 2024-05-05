import sys

def solve():
    n, t = map(int, input().split())
    fraction = float(input())

    dp = [[0] * (t + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(t + 1):
            if i == 1:
                dp[i][j] = min(int(fraction * 10 ** i), t)
            else:
                rounded_grade = int((fraction * 10 ** i) // (10 ** (i - 1))) + 1
                dp[i][j] = max(dp[i-1][j], rounded_grade, dp[i-1][j-1])

    print(max(int(fraction * 10 ** n), dp[n][t]))

if __name__ == "__main__":
    solve()
