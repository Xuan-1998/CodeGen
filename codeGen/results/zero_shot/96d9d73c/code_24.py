n, k, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

i = 0
while i < n and arr[i] + m >= arr[0]:
    i += 1

if i < k:
    print(False)
else:
    for j in range(i, n):
        if abs(arr[j] - arr[0]) > m:
            print(False)
            break
    else:
        print(True)
