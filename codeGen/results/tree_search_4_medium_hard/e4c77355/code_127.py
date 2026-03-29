def longest_increasing_subsequence(seq):
    n = len(seq)
    dp = [[1] * (n+1) for _ in range(n+1)]
    
    max_length = 0
    
    for i in range(1, n+1):
        for j in range(i):
            if seq[i-1] > seq[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        max_length = max(max_length, max(dp[i]))
    
    return max_length

if __name__ == "__main__":
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print(longest_increasing_subsequence(sequence))
