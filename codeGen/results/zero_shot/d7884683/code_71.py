n = int(input())
array = list(map(int, input().split()))
total_sum = sum(array)
left_sum = 0
max_partitions = 0

for i in range(n):
    left_sum += array[i]
    right_sum = total_sum - left_sum
    if left_sum == right_sum:
        max_partitions += 1
    elif left_sum > right_sum and i < n-1:
        for j in range(i+1, n):
            right_sum -= array[j]
            if left_sum == right_sum:
                max_partitions += 1
                break

print(max_partitions)
