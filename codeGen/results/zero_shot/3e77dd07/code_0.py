# Example 1: True (s2 is a scrambled version of s1)
s1 = "abc"
s2 = "cab"
print(is_scrambled(s1, s2))  # Output: True

# Example 2: False (s2 is not a scrambled version of s1)
s1 = "abc"
s2 = "def"
print(is_scrambled(s1, s2))  # Output: False
