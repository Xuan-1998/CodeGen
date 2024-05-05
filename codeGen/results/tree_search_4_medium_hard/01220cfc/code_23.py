from collections import deque

def canJump(nums):
    n = len(nums)
    dp = {n - 1: True}

    for i in range(n - 2, -1, -1):
        if dp.get(i + nums[i] + 1):
            dp[i] = True
        else:
            dp[i] = False

    return dp[0]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(canJump(nums))
