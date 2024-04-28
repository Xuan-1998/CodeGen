n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
for i in range(n):
    for j in range(i+1, n+1):
        if max(arr[i:j]) > k:
            count += 1
print(count)
