import sys

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Sort the sequence in ascending order
    a.sort()
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i - 1, n // 2 + 1):
            if a[j] == a[i]:
                # If the last element is equal to j or j - 1 (or j + 1 if j is at the start of the sequence), 
                # we can delete elements and their neighboring elements
                dp[i][j] = dp[i - 1][j - 1] + i
            else:
                # Otherwise, we just copy the result from the previous subsequence
                dp[i][j] = dp[i - 1][j]
    
    return max(dp[n])

print(solve())
