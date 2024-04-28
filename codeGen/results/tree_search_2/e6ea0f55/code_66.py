import sys

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-1][j])

    return max(max(row) for row in dp)

if __name__ == "__main__":
    nums = [list(map(int, input().split())) for _ in range(int(input()))]
    k = int(input())
    print(max_sum_subsequence(nums[0], k))
