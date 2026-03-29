import sys

def update_state(n):
    n = str(n)
    result = ''
    for digit in n:
        result += str(int(digit) + 1)
    return len(result), int(result)

t = int(input())
dp = {}

for _ in range(t):
    n, m = map(int, input().split())
    log_n = len(str(n))
    
    dp[0] = {j: j for j in range(1, log_n + 1)}
    
    for i in range(m + 1):
        for j in range(max(1, log_n - i), min(log_n, m + n)):
            if str(j) in str(dp[i-1]).split()[1:]:
                dp[i][j] = len(str(dp[i-1][str(j)])) + 1
            else:
                dp[i][j] = 0
    
    print(len(str(dp[m].get(max(dp[0])))) % (10**9 + 7))
