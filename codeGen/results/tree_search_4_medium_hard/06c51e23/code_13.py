import sys

def max_grade(n, t):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if not (t % 10):
            dp[i] = dp[i - 1]
        else:
            prev_max = dp[i - 1]
            prev_rounded_max = prev_max
            for j in range(i):
                new_grade = prev_rounded_max + 10 ** (i - 1 - j)
                if t >= 10 ** (i - 1 - j) % 10:
                    prev_rounded_max = max(prev_rounded_max, new_grade)
            dp[i] = max(dp[i - 1], prev_rounded_max)

    return int(str(dp[n]).split('.')[1].lstrip('0') or '0')

n, t = map(int, input().split())
print(max_grade(n, t))
