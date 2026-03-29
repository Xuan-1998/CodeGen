import sys

def merge(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(n):
            if p[2*i] < p[2*j]:
                dp[i+1][j+1] = 1
            elif p[2*i] > p[2*j]:
                dp[i+1][j+1] = dp[i][j]
    
    print("YES" if dp[n][n] else "NO")

solve()
