def longest_palindrome(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]
    
    # All substrings with one character are palindromes
    for i in range(n):
        dp[i][i] = True
    
    max_length = 1
    longest_pal = S[0]
    
    # Check for lengths 2 and above
    for i in range(n-1):
        for j in range(i+1, n):
            if S[i] == S[j]:
                if j-i+1 <= 2: 
                    dp[i][j] = True
                else:
                    dp[i][j] = (S[i] == S[j]) and dp[i+1][j-1]
                
                if dp[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    longest_pal = S[i:j+1]
    
    return longest_pal

# Example usage:
S = input()
print(longest_palindrome(S))
