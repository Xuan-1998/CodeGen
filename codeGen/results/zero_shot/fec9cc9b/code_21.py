def is_ladder(arr, start, end):
    increasing = False  # flag to track if we're in an increasing sequence
    decreasing = False  # flag to track if we're in a decreasing sequence

    for i in range(start, end + 1):
        if arr[i] < arr[i - 1]:
            decreasing = True
            increasing = False
        elif arr[i] > arr[i - 1]:
            increasing = True
            decreasing = False
        else:
            # we're at a local maximum or minimum; reset flags
            increasing = False
            decreasing = False

    return not (increasing and decreasing)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if is_ladder(arr, l - 1, r) else "No")
