n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    is_ladder = True
    non_decreasing = None
    for i in range(l-1, r):
        if arr[i] < arr[i+1]:
            non_decreasing = "non-decreasing"
        elif arr[i] > arr[i+1]:
            non_decreasing = "non-increasing"
            break
        else:
            is_ladder = False
            break
    print("Yes" if is_ladder and (non_decreasing == "non-decreasing" or non_decreasing is None) else "No")
