n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0]
for num in arr:
    prefix_sum.append(prefix_sum[-1] + num)

max_count = 0
left_sum = 0
for i in range(n):
    left_sum += arr[i]
    right_sum = sum(arr[i+1:])
    for j in range(i, n):
        if left_sum == right_sum:
            max_count = max(max_count, (j - i) // 2)
            break
        left_sum -= arr[i]
        right_sum += arr[j]

print(max_count)
