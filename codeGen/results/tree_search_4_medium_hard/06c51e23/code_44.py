import sys

def solve():
    n, t = map(int, input().split())
    f = float(input())

    dp = [[False] * (t + 1) for _ in range(n + 1)]

    # Base case: always possible to get 0.0 within any time limit
    for j in range(t + 1):
        dp[0][j] = True

    for i in range(1, n + 1):
        for j in range(t + 1):
            if not dp[i - 1][t - j]:
                continue
            digit = int((10 ** (n - i)) * f) % 10
            if digit >= 5:
                dp[i][j] = True
            elif digit > 4:
                dp[i][j] = False

    max_grade = 0
    for j in range(t + 1):
        if dp[n][j]:
            max_grade = n - j
            break

    return str(max_grade)

if __name__ == "__main__":
    print(solve())
