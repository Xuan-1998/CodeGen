def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    dp = [[False] * (n+1) for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(1, n+1):
        for j in range(-n, n+1):
            if j == 0:
                dp[i][j] = True
            elif a := arr[i-1]:
                dp[i][j] = (a >= -j) and dp[i-1][-j]
            else:
                dp[i][j] = (a <= -j) and dp[i-1][j+1]
    
    if any(not cell for row in dp for cell in row):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    solve()
