def longest_increasing_subsequence():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    # Initialize dp with zeros
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

print(longest_increasing_subsequence())
