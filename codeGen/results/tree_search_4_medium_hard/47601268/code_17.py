import sys

def solve():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if str(bin(i)[2]).count('0') == len(str(bin(i)[2])) - str(bin(i)[2]).count('1'):
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
    
    print(dp[n])

if __name__ == "__main__":
    solve()
