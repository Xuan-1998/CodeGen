n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
if max_val > k:
    count += len(arr)
else:
    for i in range(n):
        if arr[i] > k and all(j <= k for j in arr[:i]):
            count += 1
print(count)
