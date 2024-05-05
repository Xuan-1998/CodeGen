import sys

def is_sorted(subtable):
    return all(subtable[i] <= subtable[i+1] for i in range(len(subtable)-1))

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
tasks = [(int(i), int(j)) for i, j in (input().split() for _ in range(k))]

for l, r in tasks:
    subtable = table[l-1:r]
    if not is_sorted(subtable):
        print("No")
        sys.exit(0)
else:
    print("Yes")
