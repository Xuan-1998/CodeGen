ops = 0
for i in range(1, n):
    if arr[i] <= arr[i-1]:
        diff = arr[i-1] - arr[i] + 1
        arr[i:i+1] = [x+diff for x in arr[i:i+1]]
        ops += diff

print(ops)
