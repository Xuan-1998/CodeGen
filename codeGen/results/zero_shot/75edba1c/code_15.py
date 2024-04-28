n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
for i in range(n):
    if arr[i] > k:
        for j in range(i, n):
            if arr[j] <= k:
                break
            count += 1
print(count)
