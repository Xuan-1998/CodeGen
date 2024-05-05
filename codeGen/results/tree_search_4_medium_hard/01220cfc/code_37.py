from sys import stdin

def canJump(arr):
    dp = [False] * (len(arr) + 1)
    dp[0] = True

    for i in range(len(arr)):
        if not dp[i]:
            continue
        j = i + 1
        while j <= i + arr[i]:
            dp[j] = True
            j += 1

    return dp[-1]

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
print(canJump(arr))
