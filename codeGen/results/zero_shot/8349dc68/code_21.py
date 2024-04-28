n = int(input())
arr = list(map(int, input().split()))
k = int(input())

total_sum = 0
max_val = max(arr)

while k > 1:
    for i in range(len(arr) - k + 1):
        if arr[i:i+k].count(max(arr[i:i+k])) == k:
            total_sum += max(arr[i:i+k])
            del arr[i:i+k]
            break
    else:
        k -= 1

print(total_sum)
