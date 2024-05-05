import sys

def num_squares(n):
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

def main():
    n = int(input())
    print(num_squares(n))

if __name__ == "__main__":
    main()
