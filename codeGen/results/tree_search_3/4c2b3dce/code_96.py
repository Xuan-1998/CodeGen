def is_present(s):
    AB = "AB"
    BA = "BA"

    # Handle edge cases where a single character contains both substrings
    if s[0] in {AB[0], AB[1]} and s[1] in {AB[0], AB[1]}:
        return "YES" if s == AB or s == BA else "NO"
    if s[-1] in {BA[0], BA[1]} and s[-2] in {BA[0], BA[1]}:
        return "YES" if s == AB or s == BA else "NO"

    # Use KMP algorithm to find both substrings
    def kmp(pattern, text):
        pattern_len = len(pattern)
        text_len = len(text)

        lps = [0] * (pattern_len + 1)
        j = 1

        compute_lps_array(pattern, pattern_len, lps)

        i = 0
        j = 0

        while i < text_len:
            if text[i] == pattern[j]:
                i += 1
                j += 1

                if j == pattern_len:
                    return True

            elif j > 0:
                j = lps[j - 1]

            else:
                i += 1

        return False

    # Check for both substrings using KMP algorithm
    return "YES" if kmp(AB, s) and kmp(BA, s[:-1]) else "NO"

