n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    max_val = arr[i]
    for j in range(i+1, len(arr)+1):
        if j <= len(arr):
            max_val = max(max_val, arr[j-1])
        else:
            break
        if max_val > k:
            count += 1
print(count)
