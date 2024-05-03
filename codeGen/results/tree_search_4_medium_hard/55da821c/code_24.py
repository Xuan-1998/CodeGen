from math import inf

memo = {}

def dp(state):
    species_distribution, position = state
    
    if position in memo:
        return memo[position]
    
    min_replant = float('inf') 
    
    for i in range(1, m+1): 
        if species_distribution[-i] != i: 
            replant = 1 + dp((species_distribution[:-i], position - x[-i])) 
            min_replant = min(min_replant, replant)
    
    memo[position] = min_replant
    return min_replant

n, m = map(int, input().split())
x = []
s = []

for _ in range(n):
    s_i, x_i = map(float, input().split())
    x.append(x_i)

print(dp((s, 0)))
