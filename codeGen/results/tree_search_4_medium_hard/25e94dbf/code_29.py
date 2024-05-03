def max_distance_reachable(k, n):
    if k == 0:
        return 0
    if k == n:
        return total_distance_reachable(n)
    
    if dp.get((k, n)):
        return dp[(k, n)]
    
    max_dist = 0
    
    for i in range(min(k, n)):
        if commands[i] == 'F':
            new_dist = max_distance_reachable(k-1-i, n) + i
            max_dist = max(max_dist, new_dist)
        
    dp[(k, n)] = max_dist
    return max_dist

def total_distance_reachable(n):
    # calculate the total distance reachable without modifying any commands
    pass

n = int(input())
commands = list(input().strip())

dp = {}

print(max_distance_reachable(0, n))
