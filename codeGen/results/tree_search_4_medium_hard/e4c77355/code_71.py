def longest_increasing_subsequence_length():
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    dp = [[1] * (n + 1) for _ in range(n + 1)]
    max_length = 0
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[j - 1] > arr[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length

print(longest_increasing_subsequence_length())
