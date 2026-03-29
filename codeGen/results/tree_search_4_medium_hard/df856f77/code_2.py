def min_operations(arr):
    N = len(arr)
    dp = [float('inf')] * (N+1)
    dp[0] = 0

    for i in range(1, N+1):
        max_val = max(arr[:i])
        for j in range(i+1, max_val+1):
            if arr[i-1] <= j:
                dp[i] = min(dp[i], dp[j-1] + 1)

    return dp[-1]

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
