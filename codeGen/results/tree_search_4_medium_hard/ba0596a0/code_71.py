import sys

def can_cross_stones(stones):
    n = len(stones)
    dp = [True]  # Base case: It's always possible to reach the first stone (index 0)

    for i in range(1, n):
        k = stones[i] - stones[i-1]
        if not dp[i-1]:  # If it's not possible to reach the previous stone
            dp.append(False)
        else:
            dp.append(any(dp[j] and (stones[i] - stones[j] + 1) % 3 == 0 for j in range(i)))
    return dp[-1]

# Example usage:
n = int(input())  # Read the number of stones from stdin
stones = [int(x) for x in input().split()]  # Read the stone positions from stdin

print(can_cross_stones(stones))  # Print the result to stdout
