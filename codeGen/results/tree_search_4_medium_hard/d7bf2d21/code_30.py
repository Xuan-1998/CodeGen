import sys
from collections import defaultdict

def find_lis(arr):
    dp = [1] * len(arr)
    max_length = 0
    for i in range(len(arr)):
        if not dp[i]:
            for j in range(i):
                if arr[j] < arr[i]: 
                    dp[i] = max(dp[i], dp[j] + 1) 
            if not dp[i]:
                continue
            if dp[i] > max_length: 
                max_length = dp[i]
    return sum(1 for x in set(dp) if x == max_length)

arr = list(map(int, input().split()))
print(find_lis(arr))
