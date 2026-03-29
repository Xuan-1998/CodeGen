def is_ladder(arr, l, r):
    # Check for initial non-decreasing part
    for i in range(l, r):
        if arr[i] < arr[i-1]:
            return False  # Decrease found

    # Check for non-increasing part after initial non-decreasing part
    for i in range(r, l, -1):  # Start from the end and go backwards
        if arr[i] > arr[i-1]:
            return False  # Increase found

    return True  # Ladder found

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    result = is_ladder(arr, l, r)
    print("Yes" if result else "No")
