def shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Precompute all possible substrings of S using its suffix tree
    Z_values = [0] * (n + 1)
    for i in range(2, n + 1):
        if S[i - 1] == S[Z_values[i - 1]]:
            Z_values[i] = Z_values[i - 1] + 1
        else:
            leftmost = rightmost = Z_values[i - 1]
            while leftmost > 0 and S[leftmost - 1] != S[rightmost]:
                leftmost -= 1
            if leftmost <= rightmost:
                Z_values[i] = rightmost - leftmost + 1

    # Precompute all possible substrings of T using its suffix tree
    Z_values_t = [0] * (m + 1)
    for i in range(2, m + 1):
        if T[i - 1] == T[Z_values_t[i - 1]]:
            Z_values_t[i] = Z_values_t[i - 1] + 1
        else:
            leftmost = rightmost = Z_values_t[i - 1]
            while leftmost > 0 and T[leftmost - 1] != T[rightmost]:
                leftmost -= 1
            if leftmost <= rightmost:
                Z_values_t[i] = rightmost - leftmost + 1

    # Iterate through the substrings of S to find the shortest uncommon subsequence
    for i in range(n):
        for j in range(Z_values[i], n - i + 1):
            substring = S[i:i + j]
            if not is_subsequence(substring, T) and all(not is_subsequence(substring, t) for t in [T[:k] for k in range(m)]):
                return j

    return -1

def is_subsequence(substring, string):
    i = j = 0
    while i < len(substring) and j < len(string):
        if substring[i] == string[j]:
            i += 1
        j += 1
    return i == len(substring)
