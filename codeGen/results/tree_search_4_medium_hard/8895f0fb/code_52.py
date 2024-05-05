import sys
from collections import deque

def expectedCarries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * 10 for _ in range(N+1)]
        
        # Base case: adding two single-digit numbers has no carries
        for j in range(10):
            dp[0][j] = 0
        
        # Cumulative sum of carries for each digit
        for i in range(1, N+1):
            for j in range(9, -1, -1):  # Start from the most significant digit
                if j <= 4:   # Digits 0-4
                    dp[i][j] = min(10-j, max(0, 5-dp[i-1][min(9, j+1)]))
                else:   # Digits 5-9
                    dp[i][j] = min(5-j, max(0, 15-dp[i-1][min(9, j+1)]))
        
        # Calculate the expected number of non-zero carries
        total_pairs = N * 10
        expected_carries = sum(dp[N]) / total_pairs
        
        print(f"{expected_carries:.6f}")  # Output with 6 decimal places

if __name__ == "__main__":
    expectedCarries()
