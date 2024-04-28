n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    max_val = arr[i]
    for j in range(i+1, len(arr)+1):
        if max_val < k:
            break
        max_val = max(arr[i:j])
        if max_val > k:
            count += j - i
