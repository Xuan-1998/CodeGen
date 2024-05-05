import sys

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

dp = {}

def solve(i):
    if i == 0:
        return 0
    if (i,) in dp:
        return dp[(i,)]
    
    min_cost = sys.maxsize
    
    for j in range(len(strings[i-1])):
        reversed_string = strings[i-1][j:][::-1] + strings[i-1][:j]
        
        if strings[i-1] < reversed_string:
            cost = costs[j] + solve(i-1)
            min_cost = min(min_cost, cost)
    
    dp[(i,)] = min_cost
    return min_cost

min_cost = 0
for i in range(1, n+1):
    min_cost += solve(i)

print(min_cost if min_cost != sys.maxsize else -1)
