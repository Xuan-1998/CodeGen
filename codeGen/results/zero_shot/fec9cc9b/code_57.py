code block
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    increasing = decreasing = False
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            increasing = True
        elif arr[i] > arr[i+1]:
            decreasing = True
    if not (increasing and decreasing):
        print("Yes")
    else:
        print("No")
