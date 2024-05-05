import sys

def min_water_marks(n, marks):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            if k == 1:
                dp[i][k] = sum(marks[:i])
            else:
                dp[i][k] = min(dp[j][l] + (i - l) * marks[l - 1] for j in range(i) for l in range(1, k + 1))
    
    return min(dp[n])

n = int(input())
marks = list(map(int, input().split()))
print(min_water_marks(n, marks))
