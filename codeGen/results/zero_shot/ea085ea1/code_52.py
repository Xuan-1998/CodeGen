from itertools import combinations

n = int(input())
str1 = input()
str2 = input()

common_substrings = set()

for i in range(n):
    for j in range(i+1, n):
        substr1 = str1[i:j]
        substr2 = str2[i:j]

        if substr1 == substr2:
            common_substrings.add(substr1)

max_common_substrings = 0

for r in range(1, n+1):
    for substr in combinations(common_substrings, r):
        if len(''.join(substr)) <= n:
            max_common_substrings = max(max_common_substrings, len(substr))

print(max_common_substrings)
