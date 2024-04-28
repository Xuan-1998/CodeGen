def longestSubarray(nums):
    n = len(nums)
    max_len = 0
    curr_streak = 0
    
    for i in range(n):
        if nums[i] == 1:
            curr_streak += 1
            max_len = max(max_len, curr_streak)
        else:
            curr_streak = 0
    
    return max_len

def main():
    n = int(input())
    nums = [int(num) for num in input().split()]
    
    print(longestSubarray(nums))

if __name__ == "__main__":
    main()
