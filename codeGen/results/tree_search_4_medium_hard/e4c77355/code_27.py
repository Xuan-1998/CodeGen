import sys

def longest_increasing_subsequence():
    n = int(input())
    array = list(map(int, input().split()))
    
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

print(longest_increasing_subsequence())
