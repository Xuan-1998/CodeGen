s = input()
max_len = 0
max_palindrome = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substr = s[i:j]
        if substr == substr[::-1] and len(substr) > max_len:
            max_len = len(substr)
            max_palindrome = substr

print(max_palindrome)
