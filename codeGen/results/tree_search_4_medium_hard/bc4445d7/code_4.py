def solve():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        n = int(input())
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        
        m, k = map(int, input().split())
        primes = list(map(int, input().split()))
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        def dfs(i):
            if i == n:
                return 0
            if dp[i][i]:
                return dp[i][i]
            
            min_val = float('inf')
            for u, v in edges:
                if u == i:
                    f = sum(x * math.log2(primes[x-1]) for x in range(i+1, v+1))
                    min_val = min(min_val, dfs(v) + f)
                elif v == i:
                    f = sum(x * math.log2(primes[x-1]) for x in range(u+1, i+1))
                    min_val = min(min_val, dfs(u) + f)
            
            dp[i][i] = min_val
            return min_val
        
        ans = 0
        for u, v in edges:
            if u == 1:
                ans += dfs(v)
            elif v == n:
                ans += dfs(u)
        
        print(ans % MOD)

if __name__ == "__main__":
    solve()
