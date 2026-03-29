import sys
from typing import List

def longest_increasing_subsequence(arr: List[int]) -> int:
    n = len(arr)
    dp = [1] * n  # Initialize the dp table with all values as 1 (the longest increasing subsequence ending at each index is itself)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # Check if there's an earlier element that's smaller than the current one
                dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the longest increasing subsequence ending at index i

    return max(dp)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(longest_increasing_subsequence(arr))
