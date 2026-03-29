def find_min_changes(s, k):
    min_changes = 0
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if not find_substring(substring, k):
            min_changes += 1
    return min_changes

import sys

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    print(find_min_changes(s, k))
