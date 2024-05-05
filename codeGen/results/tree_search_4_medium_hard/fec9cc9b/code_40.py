n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    is_ladder = True
    left = l - 1
    right = r
    while left < right:
        if arr[left] > arr[left + 1]:
            is_ladder = False
            break
        left += 1
    while right > l:
        if arr[right - 1] < arr[right]:
            is_ladder = False
            break
        right -= 1
    print("Yes" if is_ladder else "No")
