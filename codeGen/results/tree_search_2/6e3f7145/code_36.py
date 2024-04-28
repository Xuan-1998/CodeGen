def longest_palindrome(S):
    n = len(S)
    p = [0] * n
    for i in range(1, n):
        if S[i-1] == S[n-i]:
            p[i] = 2 + (p[n-i-1] if i > 0 else 0)
        else:
            p[i] = max(p[i-1], 2) if i > 0 else 0
    return S[:p.index(max(p))]
