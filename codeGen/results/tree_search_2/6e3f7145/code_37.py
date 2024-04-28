def longest_palindrome(S):
    n = len(S)
    p = [0] * n

    for i in range(1, n):
        if S[i-1] == S[i]:
            p[i] = p[i-1] + 2
        else:
            j = max(0, i - p[i-1] - 1)
            while j < i and S[j] != S[i-j]:
                j += 1
            p[i] = 2 if j == i else p[j] + 2

    max_len = max(p)
    start_idx = p.index(max_len)

    return S[start_idx:start_idx+max_len]

S = input()
print(longest_palindrome(S))
