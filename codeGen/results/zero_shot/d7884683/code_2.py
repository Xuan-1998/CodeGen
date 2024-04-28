n = int(input())
total_sum = sum([int(x) for x in input().split()])

max_partitions = 0
left_sum = 0

for i, num in enumerate(sorted([int(x) for x in input().split()])):
    left_sum += num
    
    if left_sum == total_sum // 2:
        max_partitions += 1
        left_sum = 0
        
print(max_partitions)
