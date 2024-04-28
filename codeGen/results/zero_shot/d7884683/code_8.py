n = int(input())
arr = list(map(int, input().split()))
max_partitions = 0
left_sum = sum(arr[:n//2])
right_sum = sum(arr[n//2:])
for i in range(n):
    if arr[i] == 0:
        left_sum -= arr[i]
        right_sum += arr[i]
    else:
        if left_sum > right_sum:
            left_sum -= arr[i]
        elif right_sum < left_sum:
            right_sum += arr[i]
print(max_partitions)
