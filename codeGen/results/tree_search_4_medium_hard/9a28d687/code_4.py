from collections import defaultdict

def minCostToSortStrings(n, costs, strings):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Memoize the results of subproblems to avoid redundant computation
    memo = {}
    
    def dfs(i):
        if i in memo:
            return memo[i]
        
        min_cost = float('inf')
        
        for j in range(i):
            if strings[j].endswith(strings[i]):
                cost = costs[j] + costs[i]
                if cost < min_cost:
                    min_cost = cost
        
        dp[i] = min_cost
        memo[i] = min_cost
        return min_cost
    
    # Main function to calculate the minimum total cost
    total_cost = 0
    for i in range(1, n + 1):
        total_cost += dfs(i)
    
    if total_cost == float('inf'):
        return -1
    else:
        return total_cost

# Read input from standard input
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

print(minCostToSortStrings(n, costs, strings))
