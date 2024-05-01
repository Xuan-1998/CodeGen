import sys

str1 = input()
str2 = input()

def generate_substrings(s):
    N = len(s)
    substrings = set()
    for i in range(N):
        for j in range(i, N):
            substrings.add(s[i:j+1])
    return substrings

def find_common_substrings(s1_substrs, s2_substrs):
    common_substrs = {}
    for substring in s1_substrs & s2_substrs:  # intersection of two sets
        common_substrs[substring] = (s1_substrs.count(substring), s2_substrs.count(substring))
    return common_substrs

def count_non_overlapping_substrs(common_substrs):
    max_count = 0
    for substring, (count1, count2) in common_substrs.items():
        if count1 == count2:  # both strings have the same count
            max_count = max(max_count, min(count1, count2))
    return max_count

str1_substrs = generate_substrings(str1)
str2_substrs = generate_substrings(str2)

common_substrs = find_common_substrings(str1_substrs, str2_substrs)
max_non_overlapping_count = count_non_overlapping_substrs(common_substrs)

print(max_non_overlapping_count)
