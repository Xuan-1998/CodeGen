def find_LIS_length(sequence):
    n = len(sequence)
    dp = [[1] * (n + 1) for _ in range(n + 1)]
    
    max_length = 0
    
    for i in range(1, n + 1):
        for j in range(i):
            if sequence[i - 1] > sequence[j]:
                dp[i][j] = max(dp[i][j], dp[j][j] + 1)
        max_length = max(max_length, max(dp[i]))
    
    return max_length

sequence = list(map(int, input().split()))
print(find_LIS_length(sequence))
