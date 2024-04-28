def longest_palindrome(s):
    n = len(s)
    table = [[False] * n for _ in range(n)]

    # All substrings with one character are palindromes
    max_len = 1
    center = 0

    for i in range(n):
        table[i][i] = True

    # Expand from the center
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                table[i][j] = table[i+1][j-1]
            else:
                table[i][j] = False

            if table[i][j]:
                max_len = length
                center = i

    return s[center: center + max_len]

# Testing the function
s = input()
print(longest_palindrome(s))
