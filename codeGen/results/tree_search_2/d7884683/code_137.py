def max_partitions(arr):
    n = len(arr)
    dp = {}
    s = sum(arr)
    partitions = 0

    for i, x in enumerate(arr):
        if s - x == 0:
            partitions += 1
        s -= x

    return partitions

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
