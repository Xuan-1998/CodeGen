import sys

def count_binary(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i == 1 or not bin(i - 1).count('1') >= 2:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    return dp[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(count_binary(n))
