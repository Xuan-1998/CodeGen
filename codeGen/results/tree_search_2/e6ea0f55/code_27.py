def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if i - j - 1 >= 0:
                dp[i][j] = max(dp[i-1][j-1], nums[i] + dp[i-j-1][k])
            else:
                dp[i][j] = nums[i]

    return max(dp[-1])

def main():
    nums = [int(x) for x in input().split()]
    k = int(input())
    print(maxSumSubsequence(nums, k))

if __name__ == "__main__":
    main()
