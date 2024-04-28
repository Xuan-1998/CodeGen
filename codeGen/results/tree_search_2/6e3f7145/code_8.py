def longest_palindrome(s):
    memo = {(i, i): True for i in range(len(s))}
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (left, right) not in memo:
                memo[(left, right)] = True
            left -= 1
            right += 1
    
    max_length = 0
    max_palindrome = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if (i, j) not in memo:
                    expand_around_center(i, j)
                else:
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        max_palindrome = s[i:j+1]
    
    return max_palindrome

s = input()
print(longest_palindrome(s))
