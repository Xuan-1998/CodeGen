from collections import defaultdict

def longest_subarray(nums):
    if not nums:  # Edge case: Empty array
        return 0
    n = len(nums)
    
    dp = defaultdict(int)  # Memoization dictionary
    max_length = 0
    
    for i, num in enumerate(nums):
        if num == 1:
            dp[i] = dp.get(i-1, 0) + 1
        else:
            dp[i] = 0
        
        max_length = max(max_length, dp[i])
    
    return max_length

if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))
