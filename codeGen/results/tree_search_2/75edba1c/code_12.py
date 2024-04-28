def count_subarrays(N, K, arr):
    max_elements = {}
    dp = [{} for _ in range(N)]

    for i in range(N):
        if i > 0:
            max_elements[i] = max(max_elements[i-1], arr[i])
        else:
            max_elements[i] = arr[0]

        for j in range(i+1):
            if max_elements[i] > K and (j <= i//2 or not dp[j]):
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    return sum(dp[-1].values())

# Example usage:
N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(N, K, arr))
