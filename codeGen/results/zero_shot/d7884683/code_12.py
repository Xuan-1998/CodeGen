t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    max_partitions = 0
    for i in range(n//2, n):
        if sum(arr[i:]) == left_sum:
            max_partitions += 1
            left_sum = 0
            break
    print(max_partitions)
