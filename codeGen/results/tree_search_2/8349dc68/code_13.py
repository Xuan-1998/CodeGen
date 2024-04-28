from typing import List

def max_sum_after_partitioning(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n // k + 1)

    # Initialize dp[0] as the maximum value of the first subarray
    dp[0] = max(arr[:k])

    for i in range(1, n // k):
        min_val = float('inf')
        max_sum = 0

        for j in range(i * k, (i + 1) * k):
            if arr[j] > min_val:
                min_val = arr[j]
            else:
                max_sum += arr[j]

        dp[i] = max(dp[i - 1], max_sum)

    return dp[-1]
