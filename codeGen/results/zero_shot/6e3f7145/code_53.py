s = input()
max_length = 0
max_palindrome = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        palindrome = s[i:j]
        if palindrome == palindrome[::-1] and len(palindrome) > max_length:
            max_length = len(palindrome)
            max_palindrome = palindrome
print(max_palindrome)
