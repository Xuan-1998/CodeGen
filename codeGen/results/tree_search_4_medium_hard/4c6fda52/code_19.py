import sys

def min_changes(s, k):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(k - 1, n):
        for j in range(i, max(0, i - k + 1), -1):
            if s[j:j+k] in 'RGBRGBRGB...':
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + (s[j:k] != 'RGB' if k == 3 else 0)
    
    return dp[-1][-1]

def main():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        
        print(min_changes(s, k))

if __name__ == "__main__":
    main()
