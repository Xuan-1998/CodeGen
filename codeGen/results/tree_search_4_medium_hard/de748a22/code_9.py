import sys

def min_removals(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0]
        
        for j in range(i):
            if arr[j] == arr[j+1]:
                dp[i][j+1] = dp[i-1][j+1]
            else:
                dp[i][j+1] = min(dp[i-1][j+1], 1 + dp[i-j-2][j])
                
    return dp[n][n]

def main():
    input()
    n, q = map(int, input().split())
    
    arr = list(input())
    
    for _ in range(q):
        l, r = map(int, input().split())
        
        print(min_removals(arr[l-1:r]))

if __name__ == "__main__":
    main()
