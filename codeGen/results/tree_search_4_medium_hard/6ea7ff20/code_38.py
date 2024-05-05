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

def solve(n, p):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if p[2 * i - 1] < p[2 * j - 1]:
                dp[i][j] = any(merge(p[:2 * k], p[2 * k:2 * (i + j)]) == p[:2 * (k + i)] for k in range(i, j))
            else:
                dp[i][j] = any(merge(p[:2 * k], p[2 * k:2 * (j - i + k)]) == p[:2 * (k + j)] for k in range(j - i, j))
    
    return "YES" if dp[-1][-1] else "NO"

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    
    p = list(map(int, sys.stdin.readline().split()))
    
    print(solve(n, p))
