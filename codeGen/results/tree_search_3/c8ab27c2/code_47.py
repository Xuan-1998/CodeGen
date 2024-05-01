code
def uncommon_subsequence_length(s, t):
    # Calculate the longest common suffix (LCS) of two strings
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            break

    lcs_length = len(s) - i
    return max(0, lcs_length - 1)
