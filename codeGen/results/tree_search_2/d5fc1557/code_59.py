def findMaxForm(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    max_len = 0
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = max(dp[:i])
        
        max_len = max(max_len, dp[i])

    return max_len

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    print(findMaxForm(nums))

if __name__ == "__main__":
    main()
