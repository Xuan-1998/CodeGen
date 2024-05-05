from collections import defaultdict

def calculate_final_values():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    memo = defaultdict(int)
    
    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        final_value = 0
        while x <= 0 or x > n:
            break
        else:
            new_x = x + sequence[x]
            new_y = y + sequence[x]
            final_value = dfs(new_x, new_y) - sequence[x] + y
            
        memo[(x, y)] = final_value
        
        return final_value
    
    for i in range(2, n+1):
        print(dfs(i, 0))
