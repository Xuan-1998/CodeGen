def find_common_substrings():
    dp, str1, str2 = preprocess_input()

    # Find all substrings
    substrings = []
    for i in range(len(str1)):
        for j in range(i + 1):
            substring = str1[j:i+1]
            if substring:
                substrings.append(substring)

    count = 0

    # Count common non-overlapping substrings
    for s in substrings:
        if s in str1 and s in str2:
            start1, end1 = find_substring(str1, s)
            start2, end2 = find_substring(str2, s)

            while start1 < end1 and start2 < end2:
                if str1[start1:end1] == s and str2[start2:end2] == s:
                    count += 1
                    break
                start1 += 1
                start2 += 1

    return count


def find_substring(s, substring):
    for i in range(len(s)):
        if s[i:i+len(substring)] == substring:
            return i, i+len(substring)
    return None

print(find_common_substrings())
