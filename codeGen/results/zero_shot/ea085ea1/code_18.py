def find_common_substrs():
    max_common = 0
    for suf1 in str1_suf:
        for suf2 in str2_suf:
            # Check if the suffixes match
            if suf1 == suf2:
                max_common += 1

    return max_common

max_common = find_common_substrs()
print(max_common)
