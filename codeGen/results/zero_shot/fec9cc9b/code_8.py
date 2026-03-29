n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:  # decreasing
            break
        elif arr[i] < arr[i+1]:  # increasing
            continue
    else:  # reached the end of the subarray without finding a decrease or increase
        print("Yes")  # it's a ladder
    else:
        print("No")
