import sys

N = int(input())
str1 = input()
str2 = input()

# Initialize a set to store unique substrings from str1
set_str1 = set()
for i in range(N):
    for j in range(i+1, N+1):
        substring = str1[i:j]
        set_str1.add(substring)

# Initialize a set to store unique substrings from str2
set_str2 = set()
for i in range(N):
    for j in range(i+1, N+1):
        substring = str2[i:j]
        set_str2.add(substring)

# Find the maximum number of non-overlapping common substrings
max_common = 0
common_set = set_str1 & set_str2
for substring in common_set:
    count = 0
    start = 0
    while True:
        pos = str1.find(substring, start)
        if pos == -1:
            break
        start = pos + len(substring)
        count += 1
    max_common = max(max_common, count)

print(max_common)
