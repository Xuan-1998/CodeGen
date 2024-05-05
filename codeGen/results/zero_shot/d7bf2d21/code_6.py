from typing import List
import sys

def solve():
    n = int(sys.stdin.readline())
    arr: List[int] = list(map(int, sys.stdin.readline().split()))
    
    dp = [[1] * n for _ in range(n)]
    max_length = 0
    
    for i in range(n):
        for j in range(i, n):
            if arr[j] > arr[i]:
                dp[i][j] = min([dp[k][i-1] for k in range(i)]) + 1
                max_length = max(max_length, dp[i][j])
    
    return sum(1 for subseq in dp for val in subseq if val == max_length)

print(solve())
