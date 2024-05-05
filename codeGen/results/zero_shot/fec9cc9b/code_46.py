n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l-1, r):  # subtract 1 from l and r because indices are 0-based
        print("Yes")
    else:
        print("No")
