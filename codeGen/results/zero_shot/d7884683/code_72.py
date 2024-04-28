n = int(input())
arr = list(map(int, input().split()))
left_sum = 0
right_sum = sum(arr)
max_partition = 0
i = 0

while i < n:
    if left_sum == right_sum:
        max_partition += 1
        left_sum = 0
        right_sum = sum(arr[i:])
    elif left_sum <= right_sum:
        left_sum += arr[i]
    else:
        right_sum -= arr[i]
    i += 1

print(max_partition)
