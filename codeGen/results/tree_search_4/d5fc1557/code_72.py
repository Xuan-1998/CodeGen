def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = max(dp[i - 2], dp[i - 1]) if i > 1 else 0

    return max(0, *dp)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(longest_subarray(nums))

if __name__ == "__main__":
    main()
