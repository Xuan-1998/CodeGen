def longest_palindrome(s):
    n = len(s)
    table = [[0 for j in range(n)]for i in range(n)]
    max_len = 1
    start = 0
    for i in range(n):
        table[i][i] = True
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                table[i][j] = (cl == 2) or table[i+1][j-1]
                if table[i][j]:
                    if cl > max_len:
                        start = i
                        max_len = cl
    return s[start:start + max_len]
