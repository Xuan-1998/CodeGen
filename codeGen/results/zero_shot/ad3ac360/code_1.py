s = "aab"
print(min_cuts(s))  # Output: 1 (because we can partition the string into two palindromes: "aa" and "b")

s = "abcba"
print(min_cuts(s))  # Output: 0 (because the entire string is already a palindrome)
