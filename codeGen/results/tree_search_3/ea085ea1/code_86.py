def max_non_overlapping_substrings():
    str1 = input().strip()
    str2 = input().strip()

    common_substrings = {}
    max_count = 0

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if substring in str2:
                if substring not in common_substrings:
                    common_substrings[substring] = 1
                else:
                    common_substrings[substring] += 1

    max_count = max(common_substrings.values())

    print(max_count)

max_non_overlapping_substrings()
