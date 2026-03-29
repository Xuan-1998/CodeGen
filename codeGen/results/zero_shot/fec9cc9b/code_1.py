n, m = map(int, input().split())  # read n and m
arr = list(map(int, input().split()))  # read array

for _ in range(m):
    l, r = map(int, input().split())  # read query bounds
    if is_ladder(arr[l-1:r]):  # check subsegment [l, r] is a ladder
        print("Yes")
    else:
        print("No")
