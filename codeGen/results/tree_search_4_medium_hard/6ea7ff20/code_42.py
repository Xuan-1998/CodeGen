import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def check(p):
    n = len(p) // 2
    dp = [[False] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(i-1, -1, -1):
            if p[2*i-1] < p[2*j-1]:
                if not a := (j+1 <= i) and dp[j][i-j-1]:
                    dp[i][j] = True
                else:
                    for k in range(j+1, min(i+1, j+1)+1):
                        if merge(p[2*k-1:2*(k+1)-1], p[2*j-1:2*(j+1)-1]) == p[:2*i]+p[2*i:2*j]:
                            dp[i][j] = True
                            break
    
    return "YES" if any(dp[n][i] for i in range(n+1)) else "NO"


# Input
n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]

print(check(p))
