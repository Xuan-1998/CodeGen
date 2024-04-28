def find_substrings(s):
    a_count = 0
    b_count = 0

    for i in range(len(s)):
        if s[i] == 'A':
            a_count += 1
            if a_count == 2 and b_count == 1:
                return "YES"
        elif s[i] == 'B':
            b_count += 1
            if b_count == 2 and a_count == 1:
                return "YES"

    return "NO"
