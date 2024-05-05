import sys

# Initialize DP dictionary with {1: True}
dp = {1: True}

def canReach(i, lastJump):
    if i == len(stones) - 1:
        return dp[i]
    if i < 0:
        return False
    for j in range(max(0, lastJump-k-1), min(lastJump+k+2, i)):
        if canReach(j, stones[j]):
            return True
    dp[i] = False
    return False

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(canReach(0, 0))
