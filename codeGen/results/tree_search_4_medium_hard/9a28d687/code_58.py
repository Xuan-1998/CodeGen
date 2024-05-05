import sys

def min_cost(n, costs):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prev_str = ''
        min_cost = sys.maxsize
        
        for j in range(i):
            if strings[j] < prev_str:
                min_cost = min(min_cost, dp[j] + costs[i-1])
            
            prev_str = strings[j]
        
        dp[i] = min_cost
    
    return dp[n]

# Read input from stdin
n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

min_cost_val = min_cost(n, costs)
print(min_cost_val if min_cost_val != sys.maxsize else -1)
