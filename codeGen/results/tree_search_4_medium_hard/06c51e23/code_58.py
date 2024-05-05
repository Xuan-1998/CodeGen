import math

n, t = map(int, input().split())
fractional_part = float(input())

dp = [0] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    max_grade = 0
    for j in range(i):
        round_up_or_down = math.copysign(1, fractional_part - int(fractional_part)) >= 0
        grade_to_add = int((10 ** (i - 1 - j)) * fractional_part)
        if round_up_or_down:
            grade_to_add += 1
        max_grade = max(max_grade, dp[j] + grade_to_add)
    dp[i] = max_grade

print(dp[n])
