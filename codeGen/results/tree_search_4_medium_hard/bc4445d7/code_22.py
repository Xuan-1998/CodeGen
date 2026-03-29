import sys; input = sys.stdin.readline

def solve(n, parent):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n):
        dp[parent[i]][i] = 0
    
    for i in range(2, n):
        for j in range(i):
            if parent[j] == i:
                for k in range(j - 1, i):
                    dp[i][j] = min(dp[k][j], dp[i][k - 1] + 1)
    
    return sum(dp[0][i] for i in range(1, n))

T = int(input())
for _ in range(T):
    n = int(input())
    parent = [int(x) for x in input().split()]
    m = int(input())
    k = 1
    for _ in range(m):
        p = int(input())
        k *= p
    
    print(solve(n, parent) % (10**9 + 7))
