import sys
from collections import memoize

@memoize
def dfs(speed, time):
    if speed == 0 or time <= 0:
        return 0
    
    if speed > max_speed or speed < min_speed:
        return float('-inf')

    if (speed, time) in memo:
        return memo[(speed, time)]

    dist = min((time - 1) * speed + dfs(speed - 1, time - 2), 
               (max_time - time) * speed + dfs(max_speed, time - max_time))

    memo[(speed, time)] = dist
    return dist

min_speed, max_speed, time, max_allowed_change = map(int, input().split())
max_time = time

print(dfs(min_speed, time))
