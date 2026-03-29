dp = [[-1] * (10**6 + 1) for _ in range(2)]  # Initialize memoization table
print(dfs(1))  # Calculate the number of portal moves needed to reach room n+1
