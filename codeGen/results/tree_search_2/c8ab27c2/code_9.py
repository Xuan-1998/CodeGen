def find_shortest_uncommon_subsequence():
    S, T = input().split(), input().split()
    dp = [[False] * (len(T) + 1) for _ in range(len(S) + 1)]
    
    # Initialize the base cases: if the current character in S is not present in T, then the subsequence ending at that position cannot be a subsequence of T.
    for i in range(1, len(S) + 1):
        dp[i][0] = False
    for j in range(1, len(T) + 1):
        dp[0][j] = True
    
    # Fill the dp table using dynamic programming
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = not dp[i - 1][j]
    
    # Find the shortest uncommon subsequence by iterating through the dp table and keeping track of the longest prefix that is not a subsequence of T.
    max_length = 0
    for i in range(len(S), -1, -1):
        for j in range(len(T), -1, -1):
            if not dp[i][j]:
                max_length = i
                break
        else:
            continue
        break
    
    return len(S) - max_length

print(find_shortest_uncommon_subsequence())
