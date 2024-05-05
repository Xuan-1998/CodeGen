def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (n) for _ in range(n)]
    
    # Initialize base cases
    for i in range(n):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1, n):
        for j in range(1, min(i+1, n)):
            if p[2*i-1] + p[2*i] <= p[2*j+1-1] + p[2*j+1]:
                dp[i][j] = 1
    
    # Check if there's any pair of indices (i,j) such that dp[i][j]=1
    for i in range(1, n):
        for j in range(i, min(i+n, 2*n)):
            if dp[i-1][j-i]:
                print("YES")
                return
    
    print("NO")

if __name__ == "__main__":
    solve()
