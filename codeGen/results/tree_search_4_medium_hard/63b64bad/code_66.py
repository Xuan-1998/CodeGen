from collections import defaultdict

def simulate_program(a):
    memo = defaultdict(int)
    memo[0] = 0
    
    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        while x > len(a) or x <= 0:
            return -1
        
        y += a[x]
        x += a[x]
        y += a[x]
        x -= a[x]
        
        result = dfs(x, y)
        if result != -1:
            memo[(x, y)] = result
        else:
            return -1
        return result
    
    for i in range(2, len(a)+1):
        print(dfs(i-1, 0))
