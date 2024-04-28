import sys

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    n = len(arr)
    dp = {}
    
    for i in range(n):
        left_sum = sum(arr[:i+1])
        right_sum = sum(arr[i+1:])
        
        if left_sum == right_sum:
            dp[(0, i)] = 1
            for j in range(i+1, n):
                dp[(j, n-1)] = 1
                
    max_partitions = 0
    for (i, j) in dp:
        max_partitions += dp[(i, j)]
        
    print(max_partitions)
