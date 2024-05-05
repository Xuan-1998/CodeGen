n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    ladder = True
    decreasing = False
    for i in range(l, r+1):
        if arr[i] < arr[i-1]:
            decreasing = True
        elif arr[i] > arr[i-1]:
            if not decreasing:
                ladder = False
                break
    print("Yes" if ladder else "No")
