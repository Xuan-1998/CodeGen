import sys

def get_out_of_maze(n, portals):
    dp = [0] * (n + 1)
    
    # Base case: we need one move to reach room 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        if i == portals[i - 1]:
            # If the second portal leads to the current room, 
            # we can't use it yet; so, we'll count the moves from the previous room.
            dp[i] = dp[i - 1]
        else:
            # Use the minimum of the two possible paths: 
            # (a) using the first portal and then the second portal, or 
            # (b) using the second portal directly
            dp[i] = min(dp[i - 1], dp[portals[i - 1] - 1]) + 1
    
    return dp[n]

# Read input from stdin
n = int(input())
portals = [int(x) for x in input().split()]

# Calculate and print the result
print(get_out_of_maze(n, portals) % (10**9 + 7))
