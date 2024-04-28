def max_ones(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize dp array with zeros

    for i in range(1, n + 1):
        if nums[i - 1] == 1:  # If the current element is 1
            dp[i] = max(dp[i - 1], dp[i - 2] + 1) if i > 1 else 1
        else:  # If the current element is 0, reset the count
            dp[i] = 0

    max_length = 0
    for i in range(n):
        if nums[i] == 1:  # Check if the removed element is 1
            max_length = max(max_length, dp[i - 1])
        else:
            break  # If the removed element is 0, stop checking

    return max_length

def longest_subarray(nums):
    n = len(nums)
    for i in range(n):  # Remove one element from the array
        new_nums = nums[:i] + nums[i + 1:]
        print(max_ones(new_nums))  # Print the length of the longest subarray

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    longest_subarray(nums)
