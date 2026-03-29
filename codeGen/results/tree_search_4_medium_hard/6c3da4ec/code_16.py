import sys

def solution():
    n = int(input())
    s = input()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n, -1, -1):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = int(s[i])
            else:
                max_or = 0
                for k in range(i + 1, j + 1):
                    or_val = dp[i][k - 1] | int(s[k])
                    max_or = max(max_or, or_val)
                dp[i][j] = max_or
    
    max_or = 0
    current_or = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            current_or |= 1
        else:
            max_or = max(max_or, current_or)
            current_or = 0
    
    return bin(max_or)[2:]

print(solution())
