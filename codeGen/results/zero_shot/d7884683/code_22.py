t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left_sum = sum(arr[:n//2])
    max_partitions = 0
    for i in range(n // 2 + 1):
        right_sum = sum(arr[n // 2 - i:])
        if left_sum == right_sum:
            max_partitions += 1
            left_sum, right_sum = sum(arr[:i]), sum(arr[i:])
    print(max_partitions)
