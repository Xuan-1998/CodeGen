n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
for i in range(len(arr)):
    if arr[i] > k:
        for j in range(i, len(arr)):
            if arr[j] > k and arr[j] <= max_val:
                count += 1
                break
print(count)
