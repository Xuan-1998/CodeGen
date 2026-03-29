import sys

def solve():
    n, = map(int, input().split())
    w = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
    
    dp = [[0] * (max(w) + 1) for _ in range(n)]
    for i in range(n):
        for j in range(max(w)+1):
            if j <= w[i]:
                dp[i][j] = j
            else:
                dp[i][j] = w[i]
    
    for u, v, c in edges:
        for k in range(c-1, -1, -1):
            if dp[u][k+c] > 0 and k + c <= max(w):
                dp[v][max(k+c, dp[v][k+c])] = max(dp[v][k+c], j)
    
    return max(dp[-1])

if __name__ == "__main__":
    print(solve())
