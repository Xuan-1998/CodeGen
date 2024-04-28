def maxSum(nums, k):
    n = len(nums)
    dp = {(0, -1): 0}

    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            last_idx, curr_sum = (j - 1, nums[j - 1] if j > 0 else 0)
            dp[(i,)] = max(dp.get((last_idx, curr_sum), (0,)), nums[i] + curr_sum)

    return max([sum for _, sum in sorted(dp.values())])

# Read input from standard input
nums = list(map(int, input().split()))
k = int(input())

print(maxSum(nums, k))
