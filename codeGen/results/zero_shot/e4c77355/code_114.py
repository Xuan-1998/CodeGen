def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    numbers = [int(num) for num in input]
    print(longest_increasing_subsequence(numbers))
