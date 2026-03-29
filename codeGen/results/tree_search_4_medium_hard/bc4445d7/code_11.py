import sys

def solve():
    n, = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v, = map(int, input().split())
        edges.append((u, v))
    
    m, k, = map(int, input().split())
    prime_factors = list(map(int, input().split()))
    
    memo = [[[False] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    for u, v in edges:
        for i in range(k // max(prime_factors)):
            if k % (i * max(prime_factors)) == 0 and (memo[u][v][k - i * max(prime_factors)] or memo[v][u][k - i * max(prime_factors)]):
                memo[u][v][k] = True
                break
    
    dist = [float('inf')] * (n + 1)
    dist[0] = 0
    for u, v in edges:
        for k in range(k // max(prime_factors), -1, -1):
            if memo[u][v][k]:
                dist[u] = min(dist[u], dist[v] + k)
    
    print(sum((dist[i] + dist[j]) * (j - i) for i, j in edges) % (10**9 + 7))

if __name__ == "__main__":
    solve()
