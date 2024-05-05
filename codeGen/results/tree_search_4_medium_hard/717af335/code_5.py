import sys

def find_min_x(a, b):
    dp = [[sys.maxsize for _ in range(b+1)] for _ in range(a+1)]
    dp[0][0] = 0
    
    for i in range(1, a+1):
        for j in range(i):
            if j <= b:
                dp[i][j] = min(dp[i][j], max(j-i, 0))
    
    for i in range(a+1):
        for j in range(b+1):
            if i+j > b:
                break
            if i+j == b and i > 0:
                return -1
            dp[i][j] = min(dp[i][j], max(i-j, 0))
    
    return 0

a = int(input())
b = int(input())
print(find_min_x(a, b))
