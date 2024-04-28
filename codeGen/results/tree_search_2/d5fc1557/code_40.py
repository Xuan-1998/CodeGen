def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            dp[i] = 0
        elif nums[i-1] == 1:
            dp[i] = max(dp[i], dp[i-1]+1)
        else:
            dp[i] = dp[i-1]-1

    max_length = 0
    start, end = 0, n-1
    for i in range(n+1):
        if nums[i-1] == 1 and i-1 >= start:
            start = i-1
            max_length = max(max_length, end-start+1)
    return max_length

if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longestSubarray(nums))
