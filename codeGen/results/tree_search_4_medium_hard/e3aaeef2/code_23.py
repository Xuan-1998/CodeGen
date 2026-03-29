def solve():
    t = int(input())
    MOD = 10**9 + 7
    
    memo = {}
    
    def dfs(n, m):
        if (n, m) in memo:
            return memo[(n, m)]
        
        if n < 1 or m < 0:
            return 0
        
        res = -1
        for i in range(len(str(n))):
            d = int((str(n))[i])
            new_n = (d + 1) * (10 ** (len(str(n)) - i - 1))
            
            if len(str(new_n)) > n:
                return max(res, dfs(n, m-1))
            res = max(res, dfs(new_n, m-1))
        
        memo[(n, m)] = res
        return res
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(dfs(n, m) % MOD)

if __name__ == "__main__":
    solve()
