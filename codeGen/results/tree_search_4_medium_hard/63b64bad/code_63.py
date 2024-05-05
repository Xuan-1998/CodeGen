def calculate_y(n, sequence):
    memo = {}
    
    def dp(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        if x == 0:
            return y
        
        if (x > n or y < 0):
            return -1
        
        next_x = max(1, x + sequence[x-1])
        next_y = y + sequence[x-1]
        
        result = dp(next_x, next_y)
        
        memo[(x, y)] = result
        return result
    
    return dp(1, 0)

n = int(input())
sequence = list(map(int, input().split()))
for i in range(n-1):
    print(calculate_y(i+2, sequence))
