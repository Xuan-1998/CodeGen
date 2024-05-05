import sys

def lis_length(arr):
    n = len(arr)
    dp = [1] * n  
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  
                dp[i] = max(dp[i], dp[j] + 1)  
    return dp

def count_lis(arr):
    dp = lis_length(arr)
    max_len = max(dp)  
    return sum(1 for x in dp if x == max_len)  

arr = list(map(int, sys.stdin.readline().split()))
print(count_lis(arr))
