n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

max_count = 0
left_sum = 0
for i in range(1, n):
    left_sum += arr[i - 1]
    right_sum = sum(arr[i:])
    if left_sum == right_sum:
        max_count += 1

print(max_count)
