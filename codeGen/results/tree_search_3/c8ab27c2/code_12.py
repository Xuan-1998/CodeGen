def uncommonFromSentences(s1, s2):
    memo = {}
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(s1) or j == len(s2):
            return -1
        
        if s1[i] != s2[j]:
            return 1 + dfs(i+1, j+1)
        
        result = 1 + dfs(i+1, j+1)
        memo[(i, j)] = result
        return result
    
    return dfs(0, 0)

# Read input from standard input.
s1, s2 = [line.strip() for line in sys.stdin.readlines()]

# Calculate and print the shortest uncommon subsequence length.
print(uncommonFromSentences(s1[0], s2[0]))
