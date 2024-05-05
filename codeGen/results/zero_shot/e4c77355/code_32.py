import sys

def lis_length(arr):
    n = len(arr)
    dp = [0] * n
    max_length = 0

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    return max_length

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(lis_length(arr))
