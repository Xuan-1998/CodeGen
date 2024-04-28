def longest_palindrome(s):
    # Preprocess the string by inserting boundaries around each character,
    # so that all characters are considered to be centered.
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C, R = 0, 0

    for i in range(1, n-1):
        if R > C:
            C = R
            Q = 2*C-i
            P[i] = min(P[Q], R-C)
        else:
            P[i] = 0

        # Attempt to expand around the center.
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > R:
            C, R = i, i + P[i]

    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[centerIndex - maxLen: centerIndex + maxLen].replace('#', '')

s = input()
print(longest_palindrome(s))
