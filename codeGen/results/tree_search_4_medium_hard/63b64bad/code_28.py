def simulate_program(n, sequence):
    # Initialize memoization table with base case
    memo = [[-1] * (n + 1) for _ in range(n + 1)]
    
    def dfs(x, y):
        if x <= 0 or x > n:
            return -1
        if memo[x][y] != -1:
            return memo[x][y]
        
        # Perform operations and update memoization table
        next_y = y + sequence[x - 1]
        memo[x][y] = next_y
        return dfs(x + sequence[x - 1], next_y)
    
    result = []
    for i in range(2, n + 1):
        result.append(dfs(i, 0))
    
    return [str(y) for y in result]

# Read input from stdin
n = int(input())
sequence = list(map(int, input().split()))

print(*simulate_program(n, sequence), sep='\n')
