n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(n):
    max_val = arr[i]
    for j in range(i, n):
        max_val = max(max_val, arr[j])
        if max_val > k:
            count += 1
print(count)
