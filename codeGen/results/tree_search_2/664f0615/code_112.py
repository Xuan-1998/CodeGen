from sys import stdin

memo = {}

def dp(time, max_change):
    if (time, max_change) in memo:
        return memo[(time, max_change)]
    
    if time <= 0:
        return 0
    
    min_speed = max(1, min(100, initial_speed + time * max_change))
    max_speed = min(100, final_speed - time * max_change)
    
    length = 0
    for speed in range(min_speed, max_speed + 1):
        if abs(speed - (initial_speed + time * max_change)) <= max_change:
            length += 1
            length += dp(time - 1, max_change)
    
    memo[(time, max_change)] = length
    return length

initial_speed, final_speed, _, _ = map(int, stdin.readline().split())
_, max_change = map(int, stdin.readline().split())

print(dp(100, max_change))
