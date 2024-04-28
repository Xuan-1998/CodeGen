def partition_count(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n + 1):
        dp[i] = 1

    total_sum = sum(arr)
    left_sum = 0
    partitions = 1

    for i in range(n - 1, -1, -1):
        if left_sum == (total_sum - left_sum):
            partitions += 1
        else:
            j = i
            while j < n and left_sum <= (total_sum - left_sum):
                j += 1
            if j > i:
                partitions += 1
                left_sum = sum(arr[i:j])
            else:
                break

        left_sum += arr[i]

    return partitions

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_count(arr))
