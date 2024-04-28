def longest_palindromic_substring(s):
    n = len(s)
    p = [0] * n

    for i in range(n):
        p[i] = 1
        left, right = i - 1, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            p[i] += 2
            left -= 1
            right += 1

    max_length = max(p)
    start_idx = p.index(max_length)

    return s[start_idx:start_idx + max_length]
