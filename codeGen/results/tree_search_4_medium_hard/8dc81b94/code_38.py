import sys

def main():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    
    dp = [[False] * 2 for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        if arr[i - 1] <= 1:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][1]
        if arr[i - 1] > 1:
            dp[i][1] = dp[i - 1][0]
        else:
            dp[i][1] = dp[i - 1][1]
    
    print("YES" if dp[n][0] or dp[n][1] else "NO")

if __name__ == "__main__":
    main()
