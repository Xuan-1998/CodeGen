import sys

def process_input():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print('YES' if solve(a) else 'NO')

def solve(a):
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][i] = a[i - 1] == 0
        for j in range(i - 1, -1, -1):
            if j + 1 >= i:
                dp[j][j] = True
            elif a[j] % 2 != 0 or a[j + 1] % 2 != 0:
                dp[j][j + 1] = False
            else:
                dp[j][j + 1] = dp[i][i]
    
    return dp[0][n]

if __name__ == '__main__':
    process_input()
