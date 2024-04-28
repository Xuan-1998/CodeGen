def longest_palindrome_sube(string):
    n = len(string)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    longest_palindrome = ""
    
    # Single-character substrings are always palindromes
    for i in range(n):
        dp[i][i] = True
        if (2 * i + 1 < n and string[i] == string[2*i+1]):
            dp[i][2*i+1] = True
            max_length = 2*i + 1
            longest_palindrome = string[:max_length+1]
    
    # Expand around the center for longer palindromes
    for i in range(n-1):
        for j in range(i, n):
            if (string[i] == string[j]):
                if (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j - i + 1 > max_length):
                        max_length = j - i + 1
                        longest_palindrome = string[i:j+1]
    
    return longest_palindrome

# Read input from stdin and print output to stdout
input_string = input()
print(longest_palindrome_sube(input_string))
