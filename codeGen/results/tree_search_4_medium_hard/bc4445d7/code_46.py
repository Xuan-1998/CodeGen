import heapq
from collections import defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        
        m = int(input())
        prime_factors = list(map(int, input().split()))
        k = 1
        for p in prime_factors:
            k *= p
        
        memo = defaultdict(dict)
        ans = 0
        for u, v in edges:
            if (v, u) not in memo[u]:
                memo[u][v] = dp(u, v, memo)
            ans += memo[u][v]
        
        print(ans % (10**9 + 7))

def dp(u, v, memo):
    if (u, v) in memo:
        return memo[u][v]
    
    if u == v:
        return 0
    
    if (u, v) not in edges:
        return 0
    
    k = 1
    for edge in edges:
        if edge[0] == u and edge[1] != v:
            w = edge[1]
            break
        if edge[0] == v and edge[1] != u:
            w = edge[0]
            break
    else:
        return 0
    
    f_uv = dp(u, w, memo) + dp(w, v, memo) - dp(w, w, memo)
    s = min(f_uv // (f_uv.bit_length() if f_uv > 1 else 1), k)
    return s

solve()
