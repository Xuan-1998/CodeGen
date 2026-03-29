import sys

def max_grade(n, t):
    dp = [0] * (n + 1)
    max_grade = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if j == 0:
                rounded_value = int((dp[j] - 0.5) * 10)
            else:
                rounded_value = int((dp[j] - (j % 2) / 2) * 10)
            max_grade[i] = max(max_grade[i], min(9, dp[j] * 10 + rounded_value))

    return max_grade[n]

n, t = map(int, input().split())
print(max_grade(n, t))
