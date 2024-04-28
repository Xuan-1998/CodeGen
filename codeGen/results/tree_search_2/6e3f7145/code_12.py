def longest_palindrome(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]
    
    max_length = 0
    start_index = 0
    
    for i in range(n):
        for j in range(i, n):
            if S[i] == S[j]:
                if j - i < 2:
                    dp[i][j] = True
                elif j - i == 2:
                    dp[i][j] = (S[i] == S[j-1])
                else:
                    dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j]:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
                        start_index = i
    
    return S[start_index:start_index+max_length]

# Example usage:
S = input()
print(longest_palindrome(S))
