def longest_palindrome(s):
    n = len(s)
    max_length = 0
    start = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] and j - i + 1 > max_length:
                if s[i:j+1] == s[i:j+1][::-1]:
                    max_length = j - i + 1
                    start = i
    return s[start:start + max_length]
