def longest_subarray(nums):
    n = len(nums)
    max_streak = 0

    for i in range(n):
        streak = 0
        for j in range(i, n):
            if nums[j] == 1:
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 0
        max_streak = max(max_streak, streak)

    # Find the longest streak that doesn't include the last element
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            break

    return max_streak


if __name__ == "__main__":
    n = int(input())  # Read the number of elements from stdin
    nums = [int(x) for x in input().split()]  # Read the binary array from stdin
    print(longest_subarray(nums))  # Print the result to stdout
