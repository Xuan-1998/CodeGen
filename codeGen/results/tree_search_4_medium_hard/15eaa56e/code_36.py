===BEGIN CODE===
import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
tasks = []
for _ in range(k):
    l, r = map(int, input().split())
    tasks.append((l, r))

def is_sorted(c):
    max_val = float('-inf')
    for i in range(l-1, r):
        if table[i][c] > max_val:
            return False
        max_val = table[i][c]
    return True

for l, r in tasks:
    sorted_in_column = any(is_sorted(c) for c in range(m))
    print("Yes" if sorted_in_column else "No")
===END CODE===
