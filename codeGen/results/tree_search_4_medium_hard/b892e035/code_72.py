import sys

def calculate_probability():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        dp = [[0.0] * (17) for _ in range(51)]
        dp[1][8] = 1.0
        
        for i in range(2, n+1):
            count1, num1, num2 = map(int, sys.stdin.readline().split())
            for j in range(min(i, 16), -1, -1):
                dp[i][j] = (dp[i-1].index(max(dp[i-1])) + 1) / float(2 ** i)
                
        print('%.6f' % dp[n][8])

if __name__ == "__main__":
    calculate_probability()
