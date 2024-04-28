def longest_palindrome(s):
    n = len(s)
    p = [0] * n

    for i in range(1, n):
        if s[i] == s[i - 1]:
            p[i] = p[i - 1] + 2
        elif i > 1 and s[i] == s[i - 2]:
            p[i] = p[i - 2] - 1

    max_len = 0
    for i in range(n):
        if p[i] > max_len:
            max_len = p[i]

    return s[max_len // 2: max_len // 2 + max_len].lstrip()

# Read input from standard input
s = input().rstrip()

print(longest_palindrome(s))
