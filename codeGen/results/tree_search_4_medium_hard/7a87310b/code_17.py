import sys

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0] * (N+1) for _ in range(N+1)]
        
        # Base cases: count of invertible matrices when trace equals 0 or 1
        for i in range(2, N+1):
            dp[i][i-1] = 1
        
        # Fill in the rest of the table iteratively
        for i in range(N, 0, -1):
            for j in range(i-1, -1, -1):
                if j + j == i:
                    dp[j][j] = (dp[j+1][i-j-1] * i) // (i-j)
        
        # Count the number of matrices with positive determinant
        count = 0
        for i in range(1, N//2+1):
            if dp[i][N-i]:
                count += 1
        
        print(count)

if __name__ == "__main__":
    solve()
