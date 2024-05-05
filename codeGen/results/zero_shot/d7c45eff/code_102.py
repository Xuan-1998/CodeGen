def smallest_string(n, k):
    s = input().lower()
    if n == 1:
        return 'a' * (k-1) + ('a' if k > 0 else '')
    elif k < n and s[n-1] >= s[0]:
        return s[:k]
    else:
        if k <= len(s):
            return s
        else:
            return s + s[:k-len(s)]
