import sys

def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n  # Initialize DP table with 1s (length of each subsequence)

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP table

    max_length = max(dp)
    count = sum(1 for x in dp if x == max_length)

    return count

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(nums))

if __name__ == "__main__":
    main()
