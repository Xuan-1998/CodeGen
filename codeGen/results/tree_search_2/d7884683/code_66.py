def partition_count(arr):
    t, n = map(int, input().split())
    dp = [[0] * 2**14 for _ in range(10**9 + 1)]

    total_sum = sum(arr)
    left_sum = 0

    for i in range(n):
        left_sum += arr[i]
        right_sum = total_sum - left_sum
        dp[left_sum][right_sum] = max(dp[left_sum][right_sum], dp.get(left_sum, [0])[right_sum-1] + 1)

    return max(map(max, zip(*dp)))[0]

for _ in range(int(input())):
    print(partition_count(list(map(int, input().split()))))
