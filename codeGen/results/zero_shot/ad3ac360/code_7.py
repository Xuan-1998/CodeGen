def min_cuts(s):
    n = len(s)
    
    def is_palindrome(substring):
        return substring == substring[::-1]
    
    def dfs(i, j):
        if i >= j:  # base case: single character or empty string
            return 0
        
        for k in range(i, j+1):  # try cutting at different positions
            left = s[i:k]  # left part
            right = s[k:j+1]  # right part
            
            if is_palindrome(left + right[::-1]):  # if the cut creates a palindrome
                return 1 + dfs(i, k-1) + dfs(k+1, j)  # recurse with updated indices
        return float('inf')  # no palindromes found; return infinity
    
    return dfs(0, n-1)

import sys
s = input()
print(min_cuts(s))
