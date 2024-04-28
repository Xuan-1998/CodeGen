def longest_palindromic_substring(s):
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]
    
    for i in range(n):
        is_palindrome[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                is_palindrome[i][j] = is_palindrome[i+1][j-1]
            else:
                is_palindrome[i][j] = False
    
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s[i] == s[j]:
            if i + 1 > j - 1 or helper(i+1, j-1):
                result = s[i:j+1]
                memo[(i, j)] = result
                return result
        else:
            left = helper(i+1, j)
            right = helper(i, j-1)
            if len(left) > len(right):
                result = left
            else:
                result = right
            memo[(i, j)] = result
            return result
    
    longest_palindrome = ""
    
    for i in range(n):
        for j in range(i, n):
            candidate = helper(i, j)
            if len(candidate) > len(longest_palindrome):
                longest_palindrome = candidate
                
    return longest_palindrome

import sys
input_string = sys.stdin.read().strip()
print(longest_palindromic_substring(input_string))
