import sys

def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    t = input()
    
    dp = [[-1] * (len(t) + 1) for _ in range(len(t) + 1)]

    for i in range(len(t)):
        for j in range(1, len(t) - i):
            if any(s[k].endswith(t[i:i+j]) for k in range(n)):
                dp[i][j] = min(dp[i][j], dp[i][i+j-1] + 1)
            else:
                dp[i][j] = -1

    m = len(t)
    w = 0
    
    for i in range(len(t), 0, -1):
        if dp[i-1][i] > m:
            m = dp[i-1][i]
            w = i-1
        elif dp[i-1][i-1] == m:
            break

    print(m)
    for j in range(1, m+1):
        if dp[w-j][w] > dp[w-j-1][w]:
            print(w-j, w)
        else:
            w -= 1
