import sys

def solution():
    n, k = map(int, input().split())
    s = input()
    
    dp = ['' for _ in range(k + 1)]
    dp1 = ['' for _ in range(k + 1)]

    dp[0] = ''
    dp1[0] = ''

    for i in range(1, k + 1):
        if s[i - 1] <= 'z':
            dp[i] = dp[i - 1]
        else:
            dp[i] = 'z' + dp[i - 1]

        if i == 0 or not dp[i]:
            dp1[i] = dp[i]
        else:
            dp1[i] = 'z' + dp[i]

    print(dp1[k])

if __name__ == "__main__":
    solution()
