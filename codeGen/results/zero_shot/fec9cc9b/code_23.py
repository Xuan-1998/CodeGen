def is_ladder(arr, l, r):
    for i in range(l, r+1):
        if arr[i-1] > arr[i]:
            return False
        if arr[i] < arr[i-1]:
            return False
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if is_ladder(arr, l, r) else "No")
