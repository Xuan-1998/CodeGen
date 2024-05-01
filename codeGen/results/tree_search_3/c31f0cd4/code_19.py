from collections import defaultdict

def distinct_sums(nums):
    n = len(nums)
    max_sum = sum(nums)

    include_sum = [[0] * (max_sum + 1) for _ in range(n)]
    exclude_sum = [[0] * (max_sum + 1) for _ in range(n)]

    # Initialize the base cases
    include_sum[0][0] = 0
    exclude_sum[0][0] = 0

    for i in range(1, n):
        for j in range(max_sum + 1):
            if nums[i] <= j:
                include_sum[i][j] = max(include_sum[i-1][j], j - nums[i]) + nums[i]
                exclude_sum[i][j] = exclude_sum[i-1][j]
            else:
                include_sum[i][j] = include_sum[i-1][j]
                exclude_sum[i][j] = exclude_sum[i-1][j]

    # Find the maximum sum that can be obtained by including or excluding each number
    max_included_sum = 0
    for i in range(n):
        max_included_sum = max(max_included_sum, include_sum[i][max_sum])

    # Generate all distinct sums
    result = set()
    for j in range(max_sum + 1):
        if include_sum[n-1][j] > exclude_sum[n-1][j]:
            result.add(j)

    return sorted(list(result))

if __name__ == "__main__":
    N = int(input())
    nums = [int(x) for x in input().split()]
    print(" ".join(map(str, distinct_sums(nums))))
