def longest_palindrome(S):
    n = len(S)
    memo = {}
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and S[left] == S[right]:
            result = S[left:right+1]
            return result
            
        return None
        
    max_length = 0
    longest_palindrome = ""
    
    for i in range(n):
        # Odd-length palindrome centered at character i
        odd_result = expand_around_center(i, i)
        if len(odd_result) > max_length:
            max_length = len(odd_result)
            longest_palindrome = odd_result
            
        # Even-length palindrome centered at characters i and i+1
        even_result = expand_around_center(i, i + 1)
        if len(even_result) > max_length:
            max_length = len(even_result)
            longest_palindrome = even_result
            
    return longest_palindrome

