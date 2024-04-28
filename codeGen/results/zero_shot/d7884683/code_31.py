n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0]
for num in arr:
    prefix_sum.append(prefix_sum[-1] + num)

max_count = 0
left_sum = 0
for i in range(len(prefix_sum)):
    left_sum += prefix_sum[i]
    right_sum = sum(arr[:i]) - left_sum
    if right_sum == left_sum:
        max_count += 1

print(max_count)
