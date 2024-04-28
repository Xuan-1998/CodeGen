def longestSubarray(nums):
    n = len(nums)
    left = right = max_len = 0
    for i in range(n):
        if nums[i] == 1:
            right += 1
            max_len = max(max_len, right - left)
        else:
            left = i + 1
            right = 0
    return max_len

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longestSubarray(nums))
