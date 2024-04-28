def longest_palindrome(s):
    memo = {}
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            memo[(left, right)] = 1
            left -= 1
            right += 1

    max_length = 0
    max_palindrome = ""
    
    for i in range(len(s)):
        # Odd-length palindrome centered at this character
        expand_around_center(i, i)
        
        # Even-length palindrome centered at this character
        if i < len(s) - 1:
            expand_around_center(i, i+1)

    for (left, right) in memo:
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_palindrome = s[left:right+1]

    return max_palindrome

s = input()
print(longest_palindrome(s))
