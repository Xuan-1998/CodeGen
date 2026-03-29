import sys

def count_good_subsequences(a):
    MOD = 10**9 + 7
    
    n = len(a)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[j-1] % i == 0:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
    
    return dp[n][n]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    print(count_good_subsequences(a))

if __name__ == "__main__":
    main()
