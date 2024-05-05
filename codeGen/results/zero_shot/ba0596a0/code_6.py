import sys

def can_frog_cross(stones):
    n = len(stones)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        if dp[i-1]:
            for k in range(3):  # try k - 1, k, and k + 1
                j = max(0, i - (k + 1))
                if stones[j] == stones[i - 1] and abs(stones[i] - stones[i - 1]) == k:
                    dp[i] = True
                    break
    
    return dp[n]

# Read input from stdin
n = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.read().split()))

# Print the result to stdout
print(can_frog_cross(stones))
