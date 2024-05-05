import sys

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        
        dp = [[i for _ in range(k+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(1, k+1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(min(i, k), -1, -1):
                dp[i][j] = min(dp[i-1][j], dp[i-1][min(j+1, k)])
                if s[i-1] != (s[i-j-1] if i >= j else 'RGB'[j%3]):
                    dp[i][j] += 1
        
        print(min(dp[n]))

if __name__ == "__main__":
    main()
