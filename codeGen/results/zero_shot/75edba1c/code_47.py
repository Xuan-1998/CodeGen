n, k, arr = map(int, input().split())
count = 0
for i in range(len(arr)):
    max_val = arr[i]
    for j in range(i, len(arr)):
        max_val = max(max_val, arr[j])
        if max_val > k:
            count += (j - i + 1)
            break

print(count)
