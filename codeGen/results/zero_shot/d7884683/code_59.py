n = int(input())
arr = list(map(int, input().split()))
left_sum = 0
max_partitions = 0

for i in range(len(arr)):
    left_sum += arr[i]
    
    if left_sum == sum(arr[i+1:]):
        max_partitions += 1
        left_sum = 0
