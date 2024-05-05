import sys

def min_perfect_squares(n):
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = int(i ** 0.5)
        while j * j <= i:
            if i - j * j < 0:
                break
            dp[i] = min(dp[i], dp[j * j - 1] + 1)
            j -= 1

    return dp[n]

def main():
    n = int(input())
    print(min_perfect_squares(n))

if __name__ == "__main__":
    main()
