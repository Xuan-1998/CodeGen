def longest_palindrome(s):
    n = len(s)
    dp = set()
    
    for i in range(n):
        # Centered substrings (even length)
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            dp.add((left, right))
            left -= 1
            right += 1
        
        # Non-centered substrings (odd length)
        left, right = i, i+1
        while left >= 0 and right < n and s[left] == s[right]:
            dp.add((left, right-1))
            left -= 1
            right += 1
    
    # Find the longest palindromic substring
    max_len = 0
    max_palindrome = ""
    for (start, end) in sorted(dp):
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_palindrome = s[start:end+1]
    
    return max_palindrome

# Example usage:
input_string = input()
print(longest_palindrome(input_string))
