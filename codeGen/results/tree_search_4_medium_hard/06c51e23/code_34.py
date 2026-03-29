import sys

input()
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    max_grade = 0
    for j in range(i):
        digit = int(float(''.join(map(str, map(int, input().split('.'))))) * 10 ** j) % 10
        round_up = dp[j] + (digit >= 5)
        round_down = dp[j]
        max_grade = max(max_grade, round_up, round_down)
    dp[i] = max_grade

print(dp[n])
