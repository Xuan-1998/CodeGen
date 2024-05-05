def min_operations(n, p, l, r):
    dp = [0] * (n + 1)
    
    # Base case: The root node has no ancestors, so it only needs to adjust its value once.
    dp[0] = 0
    
    for i in range(1, n + 1):
        # If the current vertex has no ancestors, it only needs to adjust its value once.
        if p[i] == -1:
            dp[i] = min(r[i] - l[i] + 1, (l[i] + r[i]) // 2) + dp[0]
        else:
            # Calculate the minimum number of operations needed for the current vertex's ancestors.
            ancestors_ops = dp[p[i]]
            
            # If the current vertex's value is not in its range, add 1 to the ancestor's operations.
            if l[i] > r[p[i]]:
                ancestors_ops += 1
            
            # Calculate the minimum number of operations needed for the current vertex.
            dp[i] = min(ancestors_ops + (r[i] - l[i]) // 2, r[i] - l[i] + 1) + dp[0]
    
    return dp[n]

# Read input from stdin
n = int(input())
p = list(map(int, input().split()))
l = list(map(int, [input() for _ in range(n)]))
r = list(map(int, [input() for _ in range(n)]))

print(min_operations(n, p, l, r))
