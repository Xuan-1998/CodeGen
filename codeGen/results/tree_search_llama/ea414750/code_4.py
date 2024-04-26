def bear_substrings(s):
    L = [0] * 4  # Create lps[] for pattern "bear"
    i = 1
    length = 0

    while i < len("bear"):
        if "bear"[i] == "bear"[length]:
            length += 1
            L.append(length)
            i += 1
        elif length != 0:
            length = L[length - 1]
        else:
            i += 1

    bear_lps = L[:-1]

    result = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if "bear" in s[i:j]:
                result += 1
                break

    return result

s = input()
print(bear_substrings(s))
