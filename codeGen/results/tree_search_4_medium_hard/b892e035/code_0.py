import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [[0.0 for _ in range(n+1)] for _ in range(2**n+1)]
        for mask in range(2**(n+1)):
            if bin(mask)[2:].zfill(n+1).count('1') == 0:
                dp[mask][0] = 1
            else:
                for i in range(n):
                    p1, num1, num2 = map(float, input().split())
                    p2 = 1 - p1
                    if num1 != num2 and (mask >> i) & 1:
                        dp[mask][i+1] = max(dp[mask][i], dp[mask^(1<<i)][i])
                    else:
                        dp[mask][i+1] = dp[mask][i]
        print('%.6f' % dp[2**n-1][n])

if __name__ == '__main__':
    solve()
