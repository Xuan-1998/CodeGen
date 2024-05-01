def shortest_uncommon_subsequence(S, T):
    # Initialize a dictionary to store the longest common prefix for each state
    memo = {}
    
    def find_longest_common_prefix(i, j):
        # If we've already computed this prefix, return the result from the memo
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Compute the longest common prefix between S[:i] and T[:j]
        while i < len(S) and j < len(T) and S[i] == T[j]:
            i += 1
            j += 1
        
        # Store the result in the memo for future use
        memo[(i, j)] = (i, j)
        
        return (i, j)
    
    # Initialize the shortest uncommon subsequence length to infinity
    shortest_length = float('inf')
    
    # Iterate through S and T to find the shortest uncommon subsequence
    i = 0
    while i < len(S):
        j = 0
        while j < len(T):
            # Find the longest common prefix between S[:i] and T[:j]
            (prefix_end, _) = find_longest_common_prefix(i, j)
            
            # If there's no common prefix, this is an uncommon subsequence
            if prefix_end == i:
                shortest_length = min(shortest_length, i + 1)
                break
            
            # Move to the next uncommon subsequence
            i += prefix_end - i
            j += prefix_end - j
        
        # If we've found a shorter uncommon subsequence, return it
        if shortest_length != float('inf'):
            return shortest_length
    
    # If no uncommon subsequences were found, return -1
    return -1

# Example usage:
S = input().strip()
T = input().strip()
print(shortest_uncommon_subsequence(S, T))
