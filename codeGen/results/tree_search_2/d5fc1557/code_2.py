def longest_subarray(nums):
    n = len(nums)
    memo = {0: 0}

    def dp(i):
        if i in memo:
            return memo[i]
        if nums[i] == 1:
            return 1 + dp(i-1) if i > 0 else 1
        return max(dp(i-1), 0)

    max_length = 0
    for i in range(n):
        max_length = max(max_length, dp(i))
    return max_length

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(longest_subarray(nums))

if __name__ == "__main__":
    main()
