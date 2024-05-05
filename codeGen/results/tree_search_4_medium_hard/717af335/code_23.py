def solve(A, B):
    memo = {}
    
    def dfs(a, b):
        if (a, b) in memo:
            return memo[(a, b)]
        
        if a == 0:
            return (0, b)
        elif b == 0:
            return (a, 0)
        
        for i in range(1, a+1):
            for j in range(min(a, b)+1):
                if dfs(a-i, b-j) != (-1, -1):
                    memo[(a, b)] = (i, j-i)
                    return (i, j-i)
        
        return (-1, -1)

    X, Y = dfs(A, B)
    if X == -1:
        print(-1)
    else:
        print(X, Y)
