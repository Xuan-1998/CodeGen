n = int(input())
arr = list(map(int, input().split()))
left_sum = 0
right_sum = sum(arr)
max_partition = 0

for i in range(n):
    left_sum += arr[i]
    right_sum -= arr[n - i - 1]
    if left_sum == right_sum:
        max_partition += 1
        left_sum = 0
        right_sum = sum(arr)

print(max_partition)
