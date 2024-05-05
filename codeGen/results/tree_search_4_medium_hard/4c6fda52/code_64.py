import sys

def solve():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                if s[i - 1] != 'RGB'[j % 3]:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1].min()) + 1
                else:
                    dp[i][j] = dp[i - 1][j]
        
        print(min(dp[n]))
        
if __name__ == '__main__':
    solve()
