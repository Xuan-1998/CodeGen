def is_scrambled(s1, s2):
    if s1 == s2:  # base case: same strings
        return False

    for i in range(1, len(s1)):
        left_s1 = s1[:i]
        right_s1 = s1[i:]
        left_s2 = s2[:i]
        right_s2 = s2[i:]

        if is_scrambled(left_s1, left_s2) and is_scrambled(right_s1, right_s2):
            return True

    # handle leaf nodes (single characters)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True
