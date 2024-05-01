import sys

N = int(sys.stdin.readline())
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

common_substrings = {}

for s in [str1, str2]:
    generate_substrings(s)

max_count = find_max_non_overlapping(str1, str2)
print(max_count)
