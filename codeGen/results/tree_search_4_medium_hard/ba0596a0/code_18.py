def can_cross_stones(stones):
    memo = {}
    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i >= len(stones):
            return True
        if stones[i] - stones[i-1] % 3 != k:
            return False
        if k == 0:
            return dp(i+1, 1)
        result = dp(i+1, k-1) or dp(i+1, k) or dp(i+1, k+1)
        memo[(i, k)] = result
        return result

    for i in range(len(stones)):
        if dp(0, 0):
            return True
    return False

# Read input from stdin and print the answer to stdout
import sys
stones = list(map(int, sys.stdin.readline().split()))
print(can_cross_stones(stones))
