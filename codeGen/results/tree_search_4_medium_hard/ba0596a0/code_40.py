import sys

def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * (n + 1)  # initialize DP table
    dp[0] = True  # base case: frog starts on the first stone

    for i in range(1, n):
        for j in range(i):
            if dp[j] and abs(stones[i] - stones[j]) % len(stones) in [len(stones) - 1, len(stones), len(stones) + 1]:
                dp[i] = True
                break

    return dp[-1]

# Example usage:
n_stones = int(input())
stones = list(map(int, input().split()))
print(can_cross_stones(stones))
