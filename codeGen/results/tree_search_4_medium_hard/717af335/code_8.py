def find_solution(A, B):
    memo = {}

    def dfs(X, Y):
        if (X, Y) in memo:
            return memo[(X, Y)]
        
        if A == X + Y and B == X ^ Y:
            return 0
        
        min_distance = float('inf')
        for dx in range(2):
            for dy in range(2):
                if abs(X - (dx - 1)) + abs(Y - (dy - 1)) < min_distance:
                    new_X = X + dx - 1
                    new_Y = Y + dy - 1
                    
                    distance = dfs(new_X, new_Y) + 1
                    if A == new_X + new_Y and B == new_X ^ new_Y:
                        min_distance = distance
        
        memo[(X, Y)] = min_distance if min_distance != float('inf') else -1
        return memo[(X, Y)]

    X = 0
    while True:
        for dx in range(2):
            for dy in range(2):
                new_X = X + dx - 1
                new_Y = A - new_X
                
                if B == new_X ^ (A - new_X):
                    return f"{new_X} {A - new_X}"
                
                new_Y = Y + dy - 1
                if B == X ^ (Y - (dy - 1)):
                    return f"{X} {(dy - 1) * 2 - Y}"
        
        X += 1

    return "-1"
