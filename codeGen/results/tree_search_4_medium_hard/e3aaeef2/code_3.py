import sys

dp = [[0 for _ in range(200005)] for _ in range(1000005)]

def get_length(n):
    temp = str(n)
    length = len(temp)
    return length

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if dp[n][m] != 0:
            print(dp[n][m])
        else:
            length = get_length(n)
            for i in range(m+1):
                if i == 0:
                    dp[n][i] = length
                else:
                    temp = 0
                    for digit in str(n):
                        temp = (temp * 10 + int(digit) + 1) % (10**9 + 7)
                    dp[n][i] = dp[temp][i-1]
            print(dp[n][m])

solve()
