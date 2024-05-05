import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    subseg = arr[l-1:r]
    flag_decrease = False
    flag_increase = False
    for i in range(1, len(subseg)):
        if subseg[i] < subseg[i-1]:
            flag_decrease = True
        elif subseg[i] > subseg[i-1]:
            flag_increase = True
    if not flag_decrease and not flag_increase:
        print("Yes")
    else:
        print("No")
