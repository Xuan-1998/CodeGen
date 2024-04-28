def longest_palindrome(s):
    n = len(s)
    p = [0] * n

    for i in range(1, n):
        if s[i] == s[i-1]:
            p[i] = 2 + (if i > 0: p[i-1])
        else:
            p[i] = p[i-1] - 1

    max_len = 0
    center_index = 0
    for i in range(n):
        if p[i] > max_len:
            max_len = p[i]
            center_index = i

    return s[center_index - max_len: center_index + max_len]

s = input()
print(longest_palindrome(s))
