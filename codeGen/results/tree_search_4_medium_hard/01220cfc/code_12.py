def canJump(arr):
    dp = [False] * len(arr)
    dp[0] = True

    for i in range(1, len(arr)):
        if dp[i - 1]:
            for j in range(i - 1, -1, -1):
                if arr[j] <= i - j:
                    dp[i] = True
                    break

    return dp[-1]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(canJump(arr))
