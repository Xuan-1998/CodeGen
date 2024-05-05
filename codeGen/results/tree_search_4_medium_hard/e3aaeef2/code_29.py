def solve(memo):
    def dfs(n, m):
        if (n, m) in memo:
            return memo[(n, m)]
        
        if n < 10:
            return len(str(n))
        
        res = 0
        while n > 0:
            digit = n % 10
            n //= 10
            res += 1 + digit
        return (res + m) % (10**9 + 7)
    
    memo = {}
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(dfs(n, m))
