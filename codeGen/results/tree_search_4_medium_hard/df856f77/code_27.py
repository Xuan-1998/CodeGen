def min_operations(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = min(dp[i - 1], 1)
    
    return dp[-1]

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
