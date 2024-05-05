def is_ladder(arr, l, r):
    for i in range(l, r+1):
        if arr[i] < arr[i-1]:
            return False  # Decreasing sequence found
        if arr[i] > arr[i+1]:
            return False  # Increasing sequence found
    return True  # Ladder found

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
