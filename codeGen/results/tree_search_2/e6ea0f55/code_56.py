import sys

def max_sum_of_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i+1, k)+1):
            if i == 0:
                dp[i][j] = nums[i]
            else:
                max_sum = -sys.maxsize
                for window_start in range(max(0, i-j), i+1):
                    max_sum = max(max_sum, dp[window_start][j-1] + nums[i])
                dp[i][j] = max_sum

    return max([dp[i][k] for i in range(n)])

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(max_sum_of_subsequence(nums, k))
