import sys
from math import gcd
from typing import List

def min_operations_to_make_all_elements_one(n: int, arr: List[int]) -> int:
    # Step 2: Check if there is any 1 in the array
    if 1 in arr:
        return n - arr.count(1)
    
    # Step 3: Initialize dp array
    dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0

    # Step 4: Recursion and Step 5: GCD Calculation
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
                if gcd(arr[i], arr[k + 1]) == 1:
                    dp[i][j] = min(dp[i][j], j - i)

    # Step 6: Answer
    if dp[0][n - 1] == float('inf'):
        return -1
    else:
        return dp[0][n - 1]

# Read input from stdin
n = int(input().strip())
arr = list(map(int, input().strip().split()))

result = min_operations_to_make_all_elements_one(n, arr)
print(result)

