def find_uncommon_subsequence_length():
    S = input().strip()
    T = input().strip()

    # Create a dictionary to store the memoized results
    memo = {}

    def lcs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        if S[i-1] == T[j-1]:
            result = 1 + lcs(i-1, j-1)
        else:
            result = max(lcs(i-1, j), lcs(i, j-1))

        memo[(i, j)] = result
        return result

    # Find the length of the longest common subsequence between S and T
    lcs_length = lcs(len(S), len(T))
    
    # Initialize variables to store the minimum uncommon subsequence lengths
    min_length = float('inf')
    current_length = 0
    
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if (j-1 < len(T) and S[i:j] not in [T[k:i+k-j+1] for k in range(j-i)]) or j > len(T):
                current_length = j - i
                min_length = min(min_length, current_length)
    
    return min_length

print(find_uncommon_subsequence_length())
