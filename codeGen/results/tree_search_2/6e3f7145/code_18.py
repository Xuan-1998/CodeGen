def longest_palindromic_substring(s):
    n = len(s)
    table = [[0 for _ in range(n)] for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    max_length = 1
    
    for i in range(n):
        table[i][i] = True
    
    start = 0
    end = 0
    
    # Check for substring of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            end = i + 1
            max_length = 2
        else:
            table[i][i + 1] = False
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if table[i + 1][j - 1]:
                    table[i][j] = True
                    if length > max_length:
                        start = i
                        end = j
                        max_length = length
                else:
                    table[i][j] = False
    
    return s[start:end+1]

s = input()
print(longest_palindromic_substring(s))
