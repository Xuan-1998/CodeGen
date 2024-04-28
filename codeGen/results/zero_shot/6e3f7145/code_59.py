s = input()
max_length = 0
palindrome = ""
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substr = s[i:j]
        if substr == substr[::-1] and len(substr) > max_length:
            max_length = len(substr)
            palindrome = substr
print(palindrome)
