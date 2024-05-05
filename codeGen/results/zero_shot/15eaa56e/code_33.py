import sys

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(sys.stdin.readline())

for task in range(k):
    l, r = map(int, sys.stdin.readline().split())
    subtable = [row[i] for i in range(m) if l <= i < r+1]

    sorted_subtable = sorted(subtable)
    if subtable == sorted_subtable:
        print("Yes")
    else:
        print("No")
