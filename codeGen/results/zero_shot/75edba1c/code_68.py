n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
for i in range(n):
    if arr[i] > k:
        count += 1
print(count)
