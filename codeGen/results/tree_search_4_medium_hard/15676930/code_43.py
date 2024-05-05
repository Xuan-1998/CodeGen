from sys import stdin

def read_input():
    n = int(stdin.readline())
    a = [int(x) for x in stdin.readline().split()]
    b = [int(x) for x in stdin.readline().split()]
    c = [int(x) for x in stdin.readline().split()]
    return n, a, b, c

def max_joy(n, a, b, c):
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case
    dp[0][0] = c[0]
    
    for i in range(1, n+1):
        for j in range(min(i+1, n)+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + a[i-1]
            elif j == 1:
                dp[i][j] = max(dp[i-2][0] + c[i-1], dp[i-1][1] + b[i-1])
            else:
                dp[i][j] = max(dp[i-1][j-1] + c[i-1], dp[i-1][j] + b[i-1])
    
    return dp[n][n]

if __name__ == "__main__":
    n, a, b, c = read_input()
    print(max_joy(n, a, b, c))
