import sys

def solution():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        value = values[i - 1]
        if (value ^ (i % 2)) == 0:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
        
        for j in range(1, min(i, k) + 1):
            if i % 2 == 0:
                dp[i][j] = dp[(i // 2) - 1][j]
            else:
                left_xor = value ^ values[(i - 1) // 2]
                dp[i][j] = (dp[(i - 1) // 2][j] and left_xor == value)
        
        if i % 2 == 0:
            parent_value = values[(i // 2) - 1]
        else:
            parent_value = values[(i - 1) // 2]
        dp[i][k] = (dp[(i - 1) // 2][k] and value == parent_value)
    
    for i in range(n, -1, -1):
        if dp[i][k]:
            return "YES"
    return "NO"

print(solution())
