n = int(input())
left_sum = 0
right_sum = sum(input().split()) - left_sum
max_partitions = 0

for i in range(n):
    if i % 2 == 0:
        left_sum += int(input())
    else:
        right_sum -= int(input())

    if left_sum == right_sum:
        max_partitions += 1
        left_sum = 0
        right_sum = sum(input().split()) - left_sum

print(max_partitions)
