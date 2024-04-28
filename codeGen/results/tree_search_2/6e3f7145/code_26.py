for i in range(len(S)):
    for j in range(i + 1):
        if S[i] == S[j] and (j + 1 < i or dp[i - 1][j - 1]):
            dp[i][j] = True

# Find the longest palindromic substring
max_len_palindrome = 0
longest_palindrome = ""

for i in range(len(S)):
    for j in range(i + 1):
        if dp[i][j]:
            current_palindrome = S[j:i + 1]
            if len(current_palindrome) > max_len_palindrome:
                max_len_palindrome = len(current_palindrome)
                longest_palindrome = current_palindrome

print(longest_palindrome)
