import sys

def lis_length(arr):
    n = len(arr)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_len = max(dp)
    
    count = 0
    for i in range(n):
        if dp[i] == max_len:
            count += 1
            prev_idx = i
            while prev[prev_idx] != -1:
                prev_idx = prev[prev_idx]
            idx = prev_idx + 1
            subsequence = []
            while idx < n and arr[idx] > arr[prev_idx]:
                subsequence.append(arr[idx])
                idx += 1
            print(subsequence)
    
    return count

# Read the array from stdin
arr = list(map(int, input().split()))

print(lis_length(arr))
