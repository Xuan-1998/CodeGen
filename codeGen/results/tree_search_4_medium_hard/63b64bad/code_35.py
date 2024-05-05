def simulate_program(sequence):
    memo = {}
    
    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        if x <= 0 or x > len(sequence):
            return y
        
        new_x = max(1, min(len(sequence), x + sequence[x - 1]))
        new_y = y + sequence[x - 1]
        
        memo[(x, y)] = dfs(new_x, new_y)
        
        return memo[(x, y)]
    
    final_ys = []
    for i in range(2, len(sequence) + 1):
        final_ys.append(dfs(i, 0))
    
    return final_ys

n = int(input())
sequence = list(map(int, input().split()))
print(*simulate_program(sequence), sep='\n')
