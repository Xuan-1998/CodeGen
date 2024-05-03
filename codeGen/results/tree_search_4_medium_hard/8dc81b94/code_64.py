from sys import stdin

dp = [[[False] * 1001 for _ in range(301)] for _ in range(301)]

def canMakeEqualZero():
    n, k = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    
    for i in range(n+1):
        dp[i][0][k] = True
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if not dp[i-1][j][k]: continue
            if j == 1:
                dp[i][j][k] = True
            else:
                for z in range(j):
                    if not dp[i-j-1][z][k-z]:
                        break
                    dp[i][j-k+z][k] = True
    
    res = False
    for i in range(min(n+1, k)+1):
        if dp[n][i][k]: 
            res = True; break
    return "YES" if res else "NO"

for _ in range(int(stdin.readline())):
    print(canMakeEqualZero())
