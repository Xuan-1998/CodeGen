import sys
from typing import List

def longest_increasing_subsequence(nums: List[int]) -> int:
    if not nums:
        return 0

    dp = [[1] * (max(nums) + 1) for _ in range(len(nums))]

    for i, num in enumerate(nums):
        for j in range(num - 1, -1, -1):
            if dp[i][j] < dp[i-1][j] + 1:
                dp[i][j] = dp[i-1][j] + 1

    return max(max(row) for row in dp)

if __name__ == "__main__":
    nums = [int(x) for x in sys.stdin.readline().split()]
    print(longest_increasing_subsequence(nums))
