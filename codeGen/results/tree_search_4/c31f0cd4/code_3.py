from collections import defaultdict

def subsetSums(nums):
    # Initialize dp[0][i] = 1 for all i (base case: empty set generates only one subset, which is the empty set itself)
    dp = [[1] * (sum(nums) + 1) for _ in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        for j in range(1, sum(nums) + 1):
            if nums[i - 1] <= j:
                # If ai <= j, then add 1 to dp[i-1][j-ai]
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + (dp[i - 1][j] if i > 0 else 0)
            else:
                # Otherwise, just copy the result from dp[i-1][j]
                dp[i][j] = dp[i - 1][j]

    return [i for i in range(sum(nums) + 1) if dp[-1][i]]

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    print(' '.join(map(str, subsetSums(nums))))
