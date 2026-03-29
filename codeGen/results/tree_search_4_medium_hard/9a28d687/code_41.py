import sys

def f(n):
    max_len = 0
    min_cost = float('inf')
    
    dp = [[-1 for _ in range(max_len+1)] for _ in range(n+1)]
    
    # base cases
    for i in range(n+1):
        if i == 0:
            dp[i][0] = 0
        elif len(s) <= 1:
            dp[i][len(s)] = c
        
    for i in range(1, n+1):
        j = 0
        while j <= len(s[i-1]):
            if s[i-1][:j+1] < s[i-2][:j+1]:
                dp[i][j] = min(dp[i][j], dp[i-1][max(j, len(s[i-1])-len(s[i-1][:j+1]))] + c)
            j += 1
    
    if dp[n][max_len] == -1:
        return -1
    else:
        return dp[n][max_len]

n = int(input())
c = []
s = []

for _ in range(n):
    cost, string = input().split()
    c.append(int(cost))
    s.append(string)

print(f(n))
