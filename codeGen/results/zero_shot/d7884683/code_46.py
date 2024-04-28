n = int(input())
total_sum = sum(map(int, input().split()))
left_sum = 0
max_partition = 0
for i in range(n):
    left_sum += map(int, input().split())[i]
    if left_sum == total_sum // 2:
        max_partition += 1
        left_sum = 0
print(max_partition)
