import math

def min_perfect_squares(n):
    dp = {0: 0}
    for i in range(1, n + 1):
        if i not in dp:
            continue
        j = int(math.sqrt(i))
        while j * j <= i:
            j -= 1
        for k in range(j, -1, -1):
            if k * k <= i and (i - k * k) not in dp or dp[i - k * k] + 1 < dp.get(i, float('inf')):
                dp[i] = min(dp.get(i, float('inf')), dp[i - k * k] + 1)
    return dp.get(n, float('inf'))

n = int(input())
print(min_perfect_squares(n))
