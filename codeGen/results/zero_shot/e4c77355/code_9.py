import sys
from typing import List

def longest_increasing_subsequence(arr: List[int]) -> int:
    if not arr:
        return 0
    
    dp = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)
