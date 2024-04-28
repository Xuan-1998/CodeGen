def longest_subarray(nums):
    max_len = 0
    current_streak = 0

    for num in nums:
        if num == 1:
            current_streak += 1
            max_len = max(max_len, current_streak)
        else:
            if current_streak > 0:
                current_streak -= 1

    return max_len

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))
