def longest_common_subsequence(s, t):
    memo = {}
    
    def lcs_helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        if s[i-1] == t[j-1]:
            memo[(i, j)] = 1 + lcs_helper(i-1, j-1)
        else:
            memo[(i, j)] = max(lcs_helper(i-1, j), lcs_helper(i, j-1))
        
        return memo[(i, j)]
    
    def find_length_of_shortest_uncommon_subsequence(S, T):
        lcs_length = longest_common_subsequence(S, T)
        return len(S) - lcs_length

S = input().strip()
T = input().strip()
print(find_length_of_shortest_uncommon_subsequence(S, T))
