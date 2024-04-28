n, k, arr = map(int, input().split())
count = 0
max_val = max(arr)
for i in range(n):
    for j in range(i+1, n+1):
        subarr = arr[i:j]
        if max(subarr) > k:
            count += 1
print(count)
