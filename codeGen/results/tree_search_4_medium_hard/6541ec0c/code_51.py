import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    dp = [[defaultdict(int) for _ in range(20)] for _ in range(n)]
    
    for i in range(n):
        for j in range(k+1):
            xor_val = 0
            for prev_node in range(i):
                if (values[prev_node] ^ values[i]) & 1:
                    xor_val ^= (1 << ((n-1) - 1))
                dp[i][j][xor_val] = 1
    
    for u, v in edges:
        for j in range(k+1):
            for i in range(20):
                if not dp[u-1][j][i]:
                    break
            for i in range(20):
                if not dp[v-1][j][i]:
                    break
            xor_val = values[u] ^ values[v]
            for j in range(k+1):
                if dp[u-1][j][i^xor_val]:
                    dp[v-1][j][xor_val] = 1
    
    for i in range(n):
        if not dp[i][k][0]:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    solve()
