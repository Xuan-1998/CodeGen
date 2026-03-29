def partition_palindromes(S):
    N = len(S)
    dp = [[False] * (N + 1) for _ in range(N + 1)]
    
    for i in range(N + 1):
        dp[i][i] = True
    
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length
            if S[i] == S[j - 1]:
                dp[i][j - 1] = dp[i + 1][j - 2]
    
    partitions = []
    for i in range(N):
        for j in range(i, N):
            if dp[i][j]:
                partition = [S[k] for k in range(i, j + 1)]
                partitions.append(partition)
    
    return partitions

if __name__ == "__main__":
    S = input()
    print(partition_palindromes(S))
