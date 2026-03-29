code
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    if all(arr[i] <= arr[i+1] for i in range(l-1, r-1)):
        if all(arr[i] >= arr[i+1] for i in range(r-1, l, -1)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
