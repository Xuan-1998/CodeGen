from sys import stdin

def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = nums[i - 1]
            else:
                max_sum = nums[i - 1]
                for prev_index in range(max(0, i - k - 1), i):
                    max_sum = max(max_sum, dp[prev_index][j - 1] + nums[i - 1])
                dp[i][j] = max_sum

    return dp[-1][-1]

if __name__ == "__main__":
    nums = list(map(int, stdin.readline().split()))
    k = int(stdin.readline())
    print(max_sum_subsequence(nums, k))
