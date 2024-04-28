def maximum_ones(nums):
    max_len = 0
    curr_streak = 0

    for num in nums:
        if num == 1:
            curr_streak += 1
            max_len = max(max_len, curr_streak)
        else:
            if curr_streak > 0:
                max_len = max(max_len, curr_streak)
                curr_streak = 0

    return max_len


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    
    print(maximum_ones(nums))
