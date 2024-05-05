n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if is_ladder(arr, l-1, r) else "No")
