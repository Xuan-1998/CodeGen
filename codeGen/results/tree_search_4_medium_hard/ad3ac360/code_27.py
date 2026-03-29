def minCut(s):
    n = len(s)
    table = [[False] * n for _ in range(n)]
    
    # Base cases: single character and empty string are always palindromes
    for i in range(n):
        table[i][i] = True
    
    # Fill up the table in bottom-up manner
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            
            # Check if the substring is palindromic
            if s[i] == s[j] and (length == 2 or table[i+1][j-1]):
                table[i][j] = True
    
    # Count the minimum number of cuts needed by iterating through the table
    max_consecutive_palindromes = 0
    min_cuts = 0
    
    for i in range(n):
        if not table[0][i]:
            min_cuts += 1
        else:
            max_consecutive_palindromes = i + 1
    
    return min_cuts

# Receive input from stdin and print the output to stdout
s = input()
print(minCut(s))
