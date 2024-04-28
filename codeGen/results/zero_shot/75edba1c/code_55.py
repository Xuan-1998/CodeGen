n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
max_val = max(arr)
for i in range(n):
    if arr[i] > k:
        count += (arr[i:] + [max_val]).index(max_val) - i + 1
print(count)
