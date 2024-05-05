import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().strip()

    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        if i == 1:
            dp[i][0] = [s[0]]
        else:
            dp[i][0] = ['']
            for j in range(1, i):
                dp[i][0].extend([x + y[-1] for x in dp[j][0] for y in dp[i-j][0]])
            
    for i in range(n+1):
        for j in range(k+1):
            if i == 0 and j == 0:
                print(''.join(dp[i][j]))
                return
            if len(dp[i][j]) > 0:
                min_str = min(dp[i][j])
                print(min_str)
                return

solve()
