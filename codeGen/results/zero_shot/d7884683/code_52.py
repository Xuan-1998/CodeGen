n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0]
for x in arr:
    prefix_sum.append(prefix_sum[-1] + x)

max_partition = 0
left_sum = 0
for i in range(len(prefix_sum)):
    left_sum += prefix_sum[i]
    if left_sum == (sum(arr) - left_sum):
        max_partition += 1

print(max_partition)
