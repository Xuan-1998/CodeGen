import sys

def max_grade(n, t):
    dp = [0] * (n + 1)
    rounding_points = [0] * (n + 1)

    for i in range(1, n + 1):
        time_left = t - i
        if time_left < 0:
            break

        grade = round(10 ** (n - i))
        dp[i] = max(dp[i-1], min(dp[i-1] + grade, 100))

    return dp[n]

# Read input from stdin
n, t = map(int, input().split())

print(max_grade(n, t))
