def find_shortest_uncommon_subsequence():
    S, T = input().split()
    
    # Initialize a 2D array to store the lengths of subsequences
    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    
    # Initialize variables to keep track of the shortest uncommon subsequence
    shortest_length = float('inf')
    
    # Iterate over S and T to fill up the dp array
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If the current characters don't match, consider the maximum length of subsequences without them
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
            # Update the shortest uncommon subsequence if needed
            if i == len(S) and j == len(T):
                shortest_length = min(shortest_length, i - dp[i][j])
    
    return shortest_length

print(find_shortest_uncommon_subsequence())
