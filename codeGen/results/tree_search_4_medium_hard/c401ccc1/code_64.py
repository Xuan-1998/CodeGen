from collections import defaultdict

def infinite_zoo():
    q = int(input())
    dp = [False] * (1 << 30)
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        # Add an edge from u to v
        while u & v:
            v &= ~u
        
        if not any(dp[i] for i in range(2**30)):
            dp[v] = True
        else:
            for i in range(2**30):
                if (not any(dp[j] and (i | j) != i for j in range(2**30))):
                    dp[i] = dp[v]
        
        print("YES" if dp[u] else "NO")

if __name__ == "__main__":
    infinite_zoo()
