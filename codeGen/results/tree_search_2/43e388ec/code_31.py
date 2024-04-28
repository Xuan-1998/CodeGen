import sys

def solve():
    a, b = map(int, input().split())
    dp = [[0] * (len(bin(a)) + 1) for _ in range(len(bin(a)) + 1)]
    
    for i in range(1, len(bin(a)) + 1):
        for j in range(i):
            if j < len(bin(b)):
                dp[i][j] = (dp[i-1][j % (i+1)] if j > i else 0) + ((a >> (i-1)) ^ int('1' + '0'*j + bin(b)[len(bin(b))-1:j-1:-1],2)) * pow(2, i-1)
            else:
                dp[i][j] = (dp[i-1][j % (i+1)] if j > i else 0) + ((a >> (i-1)) ^ 0) * pow(2, i-1)
    
    print(sum(dp[-1]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
