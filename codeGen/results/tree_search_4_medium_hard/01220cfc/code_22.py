import sys

def canJump(nums):
    dp = [False] * len(nums)
    dp[0] = True

    for i in range(1, len(nums)):
        if dp[i-1]:
            for j in range(i-1, -1, -1):
                if j + nums[j] >= i:
                    dp[i] = True
                    break
        else:
            dp[i] = False

    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    jumps = list(map(int, input().split()))
    print(canJump(jumps))
