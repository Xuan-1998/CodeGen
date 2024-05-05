import sys

def min_marks_below_water(n, marks):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[j] + (n - i) for j in range(i))
    return min(dp)

n = int(input())
marks = list(map(int, input().split()))
print(min_marks_below_water(n, marks))
