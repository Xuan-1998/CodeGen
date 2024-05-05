import sys

def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]
    
    dp = [[0]*(27) for _ in range(n+1)]
    max_len = [0] * (n+1)
    
    for i in range(1, n+1):
        c = ord(s[i-1]) - 97
        j = min(i, a[c])
        for k in range(j-1, -1, -1):
            dp[i][k+1] = sum(dp[x][y] for x in range(i-1) for y in range(27) if (x-k<=0 or dp[x-k][min(k+1,a[y-1])]==0))
            max_len[i] = max(max_len[i], max_len[k]+1)
    
    print((dp[n][26]%1000000007))
    print(max_len[n])
    print(n-max_len[n])

if __name__ == "__main__":
    solve()
