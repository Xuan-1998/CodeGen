def max_partitions(arr):
    n = len(arr)
    dp = [0] * (n + 1)  # Initialize DP table

    for i in range(1, n + 1):  # Iterate over array indices
        left_sum = right_sum = total_sum = 0
        k = i - 1  # Start from the beginning of the array
        for j in range(i):
            total_sum += arr[j]
            if total_sum == arr[i - 1]:
                left_sum = i - 1
                break
            elif total_sum < arr[i - 1]:
                continue
            else:
                right_sum = k
                while k > j and total_sum >= arr[k]:
                    total_sum -= arr[k]
                    k -= 1
        dp[i] = max(dp[i - 1], left_sum // 2 + (left_sum % 2) if left_sum % 2 == 0 else right_sum // 2 + (right_sum % 2))

    return dp[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
