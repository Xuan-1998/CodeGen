from collections import defaultdict

def solve(n, sequence):
    memo = defaultdict(int)
    
    def simulate(x, y, i):
        if (x, i) in memo:
            return memo[(x, i)]
        
        if x <= 0 or x > n:
            return 0
        
        new_x = x + sequence[x]
        new_y = y + sequence[x]
        
        result = new_y
        while x + sequence[x] <= n and x > 0:
            x += sequence[x]
            y += sequence[x]
        if x <= 0 or x > n:
            return 0
        
        memo[(x, i)] = simulate(x, y, i)
        return memo[(x, i)]
    
    for i in range(1, n):
        print(simulate(i, 0, 1))
