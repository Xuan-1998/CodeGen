def solve():
    t = int(input())
    mod = 10**9 + 7
    
    dp = {}
    
    def dfs(n, m):
        if (n, m) in dp:
            return dp[(n, m)]
        
        if len(str(n)) == 1:
            return n
        
        next_n = ''
        for d in str(n):
            next_n += str(int(d) + 1)
        
        if m > 0:
            m -= 1
            next_n = str(next_n)
            dp[(n, m)] = dfs(int(next_n), m) + len(str(next_n)) - len(str(n))
        else:
            dp[(n, m)] = n
        
        return dp[(n, m)]
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(dfs(n, m) % mod)

if __name__ == "__main__":
    solve()
