def is_ladder(arr, l, r):
    # Check if array doesn't decrease
    decreasing = False
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            decreasing = True
            break

    # Check if array doesn't increase
    increasing = False
    for i in range(l, r+1):
        if arr[i-1] < arr[i]:
            increasing = True
            break

    return not (decreasing or increasing)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if is_ladder(arr, l, r) else "No")
