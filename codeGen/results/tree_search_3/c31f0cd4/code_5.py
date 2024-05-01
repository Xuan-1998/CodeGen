def get_distinct_sums(nums):
    # Initialize the dp array with zeros
    n = len(nums)
    max_sum = sum(nums)
    dp = [[False] * (max_sum + 1) for _ in range(n + 1)]

    # Base case: The sum of an empty subset is 0
    dp[0][0] = True

    # Iterate over the numbers and subsets
    for i in range(1, n + 1):
        for j in range(max_sum + 1):
            # If the current number is greater than the current sum, skip it
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Add the current number to the previous sums that add up to (j - nums[i - 1])
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # Initialize an empty set to store the distinct sums
    distinct_sums = set()

    # Iterate over the dp array and add the distinct sums to the set
    for i in range(max_sum + 1):
        if dp[n][i]:
            distinct_sums.add(i)

    return ' '.join(map(str, sorted(list(distinct_sums))))


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    print(get_distinct_sums(nums))
