def count_subarrays(arr, k):
    n = len(arr)
    dp = [0] * n
    
    for i in range(n):
        max_val = 0
        for j in range(i, -1, -1):
            max_val = max(max_val, arr[j])
            if max_val > k:
                dp[i] += (i - j + 1)
    
    return sum(dp)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(arr, k))
