def longest_palindrome(s):
    n = len(s)
    memo = [[0] * n for _ in range(n)]

    max_len = 0
    center_idx = 0

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j-i < 3: # single character or two characters that are the same
                    memo[i][j] = 1
                elif j-i == 3 and s[i] == s[j-1]: # three characters that form a palindrome
                    memo[i][j] = 1
                else:
                    if i+1 <= j-1: # check for odd length palindromes
                        memo[i][j] = memo[i+1][j-1] + 2
                    max_len = max(max_len, memo[i][j])
                    center_idx = (i+j) // 2

    return s[center_idx - max_len//2:center_idx + max_len//2]

# Example usage:
s = input()
print(longest_palindrome(s))
