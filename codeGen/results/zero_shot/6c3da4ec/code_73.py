def max_or_value(s):
    max_or = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr1 = int(s[i:j], 2)
            for k in range(j, len(s) + 1):
                substr2 = int(s[j:k], 2)
                or_val = substr1 | substr2
                max_or = max(max_or, or_val)
    return bin(max_or)[2:]
