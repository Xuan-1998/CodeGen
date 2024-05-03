import sys

n, m = map(int, input().split())

dp = {(0, 1): 0}  # Initialize dictionary with base case

for i in range(n):
    s, x = map(int, input().split())
    prev_section = dp.keys()[-1][1]
    
    if s != prev_section:  # If the current plant is of a different species
        min_replanted = float('inf')
        for section in range(1, m + 1):
            if (dp.get((0, section), float('inf')) + x - dp[(0, prev_section)][1] <= x):  
                min_replanted = min(min_replanted, dp[(0, section)] + 1)
        dp[(i + 1, prev_section)] = min_replanted
    else:  # If the current plant is of the same species as the previous one
        dp[(i + 1, prev_section)] = dp[(i, prev_section)] + 1

print(dp.get((n, m), -1))
