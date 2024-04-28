import sys
n, k, *arr = map(int, input().split())
count = 0
max_so_far = max(arr)
for i in range(len(arr)):
    if arr[i] > k:
        for j in range(i+1, len(arr)):
            if arr[j] <= k:
                break
        else:
            count += 1
print(count)
