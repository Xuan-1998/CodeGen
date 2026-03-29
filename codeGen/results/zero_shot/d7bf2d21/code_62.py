def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n
    max_length = 0
    
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    return sum(1 for x in dp if x == max_length)

sequence = list(map(int, input().split()))
print(longest_increasing_subsequence(sequence))
