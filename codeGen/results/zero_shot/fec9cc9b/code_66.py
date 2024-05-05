def is_ladder(arr, l, r):
    # Check if the subsegment is non-decreasing first
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            return False  # Not a ladder

    # If it's non-decreasing, check if it becomes non-increasing after that
    increasing = False
    for i in range(r-1, l, -1):
        if arr[i] < arr[i-1]:
            increasing = True
            break  # We've found the start of the non-increasing part

    return not increasing  # It's a ladder if it doesn't become non-increasing after the initial non-decreasing part

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Process queries and print answers to stdout
for _ in range(m):
    l, r = map(int, input().split())
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
