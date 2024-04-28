s = input()

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

max_len_palindrome = ""

for i in range(len(s)):
    # Odd length palindrome
    palindrome = expand_around_center(s, i, i)
    if len(palindrome) > len(max_len_palindrome):
        max_len_palindrome = palindrome

    # Even length palindrome
    palindrome = expand_around_center(s, i, i + 1)
    if len(palindrome) > len(max_len_palindrome):
        max_len_palindrome = palindrome

print(max_len_palindrome)
