import sys

N = int(input())  # read N from stdin
str1 = input().strip()  # read str1 from stdin
str2 = input().strip()  # read str2 from stdin

# generate all substrings for str1
substrings_str1 = set()
for i in range(N):
    for j in range(i + 1, N + 1):  # end index is inclusive
        substring = str1[i:j]
        substrings_str1.add(substring)

# generate all substrings for str2
substrings_str2 = set()
for i in range(N):
    for j in range(i + 1, N + 1):  # end index is inclusive
        substring = str2[i:j]
        substrings_str2.add(substring)

# find common non-overlapping substrings
common_substrings = set()
for substring in substrings_str1:
    if substring in substrings_str2:  # check if substring exists in str2
        common_substrings.add(substring)  # add to the set of common substrings

print(len(common_substrings))  # print the maximum number of common substrings
