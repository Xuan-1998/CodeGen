import sys

# Read input from stdin
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Preprocess the input strings
set1 = set(str1)
set2 = set(str2)

common_chars = set1 & set2

substrings1 = []
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        substrings1.append(str1[i:j])

substrings2 = []
for i in range(len(str2)):
    for j in range(i + 1, len(str2) + 1):
        substrings2.append(str2[i:j])

common_substrings = set()
for substring1 in substrings1:
    for substring2 in substrings2:
        if substring1 == substring2 and substring1 not in common_substrings:
            common_substrings.add(substring1)

print(len(common_substrings))
