n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
for i in range(n):
    for j in range(i, n):
        if max(arr[i:j+1]) > k:
            count += 1
print(count)
