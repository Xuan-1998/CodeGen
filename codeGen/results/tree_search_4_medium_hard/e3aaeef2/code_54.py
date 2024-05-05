def solve():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Read n and m for each test case
        dp = [[0] * (m + 1) for _ in range(10)]  # Initialize a dynamic programming table with size 10 x (m + 1)
        
        for i in range(1, 10):  # Initialize base cases for dp[i][j]
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[1][j] = 1
        
        for i in range(2, 10):
            for j in range(m, -1, -1):  # Iterate from right to left
                if j >= i:  # If there are enough operations left
                    dp[i][j] = min(dp[k][j - 1] for k in range(10**(i - 1), 10**i)) + 1
                else:
                    break
        
        print((dp[n][m]) % (10**9 + 7))  # Print the result after applying m operations on an n-digit number

if __name__ == "__main__":
    solve()
