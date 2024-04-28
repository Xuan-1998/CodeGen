def longest_palindrome(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]
    
    # Initialize base cases
    for i in range(n):
        dp[i][i] = True
    
    # Fill up the dynamic programming table
    max_length = 0
    longest_palindrome = ""
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
            
            # Update the longest palindromic substring
            if dp[i][j] and j - i + 1 > max_length:
                max_length = j - i + 1
                longest_palindrome = S[i:j+1]
    
    return longest_palindrome

if __name__ == "__main__":
    S = input()
    print(longest_palindrome(S))
