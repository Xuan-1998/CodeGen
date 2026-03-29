import sys

def min_squares(n):
    dp = {0: 0}
    for i in range(1, n + 1):
        dp[i] = sys.maxsize
        for j in range(int(i ** 0.5) + 1):
            if (j ** 2) <= i and i - (j ** 2) in dp:
                dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)
    return dp[n]

def main():
    n = int(input())
    print(min_squares(n))

if __name__ == "__main__":
    main()
