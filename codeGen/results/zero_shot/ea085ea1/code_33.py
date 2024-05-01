import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# Generate all substrings
substrings1 = [str1[i:j+1] for i in range(N+1) for j in range(i, N)]
substrings2 = [str2[i:j+1] for i in range(N+1) for j in range(i, N)]

# Find common non-overlapping substrings
max_common = 0
for sub1 in substrings1:
    for sub2 in substrings2:
        if sub1 == sub2 and not (str1.find(sub1) < str1.find(sub2)):
            max_common += 1

print(max_common)
