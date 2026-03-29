import sys

def find_longest_increasing_subsequences():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Create a 2D table for dynamic programming
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    max_length = 0
    
    for j in range(1, n):
        current_max_length = 0
        
        for i in range(j - 1, -1, -1):
            if arr[i] < arr[j]:
                current_max_length += 1
                break
            
            current_max_length += 1
        
        max_length = max(max_length, current_max_length)
        
        dp[max_length][j] = True
    
    longest_increasing_subsequences = 0
    
    for length in range(n - 1, 0, -1):
        if any(dp[length][i] for i in range(length)):
            longest_increasing_subsequences += 1
            break
    
    print(longest_increasing_subsequences)

find_longest_increasing_subsequences()
