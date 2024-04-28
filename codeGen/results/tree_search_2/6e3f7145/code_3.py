def longest_palindromic_substring(s):
    n = len(s)
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][i] = 1

    start, end = 0, 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] == s[j] and (j - i < 3 or table[i + 1][j - 1]):
                table[i][j] = 2 * (s[i] == s[j])
                if j - i > end - start:
                    start, end = i, j

    return s[start:end+1]

# Read input from stdin
s = input()

print(longest_palindromic_substring(s))
