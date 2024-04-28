from collections import defaultdict
from typing import Dict

def max_sum_after_partitioning(arr: list[int], k: int) -> int:
    n = len(arr)
    dp: Dict[int, int] = defaultdict(int)

    for i in range(k - 1):
        dp[i] = sum(arr[:i + 1])

    max_sum = max(dp.values())

    for i in range(k - 1, n):
        if i < k:
            dp[i] = max(arr[:i + 1])
        else:
            dp[i] = max(dp[i - k] + arr[i - k + 1:i + 1], dp[i - 1])

        max_sum = max(max_sum, dp[i])

    return max_sum
