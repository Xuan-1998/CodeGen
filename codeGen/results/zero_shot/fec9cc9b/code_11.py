import sys

def is_ladder(arr, l, r):
    # Check for non-decreasing sequence at the start of the segment
    decreasing = False
    for i in range(l-1, r):  # iterate from l-1 to r-1 (inclusive)
        if arr[i] > arr[i+1]:
            decreasing = True
            break

    # If it's not decreasing, check for non-increasing sequence at the end of the segment
    increasing = False
    for i in range(r-1, l, -1):  # iterate from r-1 to l (exclusive)
        if arr[i] < arr[i-1]:
            increasing = True
            break

    return not decreasing and increasing

n, m = map(int, input().split())  # read n and m from standard input

arr = list(map(int, input().split()))  # read array elements from standard input

for _ in range(m):
    l, r = map(int, input().split())  # read query indices l and r
    if is_ladder(arr, l, r):
        print("Yes")
    else:
        print("No")
