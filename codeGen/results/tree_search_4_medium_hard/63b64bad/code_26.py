from collections import defaultdict

def solve():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    memo = defaultdict(lambda: -1)
    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        terminated = False
        result = 0
        
        while x <= n and x > 0:
            a_x = sequence[x-1]
            x += a_x
            y += a_x
            
            if x <= 0 or x > n:
                terminated = True
                break
            result = max(result, dfs(x, y))
        
        memo[(x, y)] = result
        return result if not terminated else -1

    for i in range(2, n+1):
        print(dfs(i, 0))

solve()
