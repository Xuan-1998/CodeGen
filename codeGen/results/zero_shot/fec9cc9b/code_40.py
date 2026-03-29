n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    decrease = False
    increase = False
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            decrease = True
        elif decrease:
            increase = True
            break
    print("Yes" if not (decrease and increase) else "No")
