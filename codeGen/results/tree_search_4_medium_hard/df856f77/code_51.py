def min_operations(arr):
    N = len(arr)
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = min(dp[i], dp[j] + abs(arr[i] - arr[j]))

    return dp[N]

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
