import sys

def largest_sum_after_partitioning(arr, k):
    n = len(arr)
    
    # Initialize the dictionary with base cases
    dp = {0: 0}
    max_sum = 0
    
    for i in range(k-1, -1, -1):
        if i + k <= n:
            subarray_sum = sum(arr[i:i+k])
            if i not in dp:
                dp[i] = subarray_sum
            else:
                dp[i] = max(dp[i], subarray_sum)
            max_sum = max(max_sum, dp[i])
    
    for i in range(k-1, n):
        if i - k + 1 >= 0 and i - k + 1 in dp:
            last_subarray_sum = sum(arr[i-k+1:i+1])
            dp[i] = max(dp.get(i-1, 0), arr[i] + dp.get(i-k, 0))
            max_sum = max(max_sum, dp[i])
    
    return max_sum

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(largest_sum_after_partitioning(arr, k))
