import sys

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i + 1, k) + 1):
            if i < j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[max(0, i - k)][j - 1], nums[i])
    
    return sum(dp[-1])

if __name__ == "__main__":
    input()
    nums = list(map(int, input().split()))
    k = int(input())
    print(maxSumSubsequence(nums, k))
