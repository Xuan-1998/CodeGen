from collections import deque

def partition_palindromes(S):
    N = len(S)
    dp = [[False] * (N + 1) for _ in range(N + 1)]
    
    # Base cases: single characters are palindromes
    for i in range(N + 1):
        dp[i][i] = True
    
    # Fill up the dp table
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length
            if S[i] == S[j]:
                dp[i][j] = (length == 2 or dp[i + 1][j - 1])
    
    # Find all possible palindromic partitions
    partitions = []
    for i in range(N + 1):
        for j in range(i, N + 1):
            if dp[i][j]:
                partition = [S[i:j+1]]
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    for k in range(x - 1, -1, -1) or range(y + 1, N):
                        if S[k] == S[y]:
                            new_partition = partition.copy()
                            new_partition.append(S[x:k])
                            queue.extend([(x, k), (k + 1, y)])
                partitions.append(new_partition)
    
    return partitions

S = input().strip()
print(partition_palindromes(S))
