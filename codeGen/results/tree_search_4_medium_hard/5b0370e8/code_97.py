import sys

def and_or_xor():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(2 ** k):
            dp[i][0] = 1
        for j in range(1, k + 1):
            for i in range(2 ** k):
                if bin(i)[2:].zfill(k).count('1') == j:
                    dp[i][j] = (dp[i][j - 1] * ((i & (2 ** (k - 1) - 1)) // (2 ** (k - 1)))) % (10 ** 9 + 7)
                else:
                    dp[i][j] = dp[i][j - 1]
        ans = 0
        for j in range(k, -1, -1):
            if n & (2 ** j - 1) == 2 ** j - 1:
                ans += dp[n][j]
            else:
                break
        print(ans % (10 ** 9 + 7))

if __name__ == "__main__":
    and_or_xor()
