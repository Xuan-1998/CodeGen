import sys

def longest_ones(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(n - 1):
        if nums[i] == 1 and (i == 0 or nums[i - 1] == 1):
            dp[i + 1] = dp[i] + 1
        else:
            dp[i + 1] = 0
    
    return max(dp)

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    print(longest_ones(nums))

if __name__ == "__main__":
    main()
