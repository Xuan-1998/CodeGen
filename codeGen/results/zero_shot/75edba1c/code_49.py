n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
max_val = max(arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
        sub_arr = arr[i:j]
        if max(sub_arr) > k:
            count += 1
print(count)
