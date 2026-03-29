import sys

def min_operations(n, x):
    dp = [0] * (n + 1)
    for i in range(1, n+1):
        max_digit = int(10**i - 1) // 9
        if x < 10**max_digit:
            dp[i] = dp[max(0, i-1)] + 1
        else:
            min_ops = sys.maxsize
            for d in range(1, 10):
                if x % 10 == d:
                    min_ops = min(min_ops, dp[max(0, i-1)] + 1)
                elif x < 10**max_digit:
                    min_ops = min(min_ops, dp[max(0, i-1)] + 1)
                else:
                    new_x = x * d
                    min_ops = min(min_ops, dp[i-1] + (new_x >= 10**i))
            dp[i] = min_ops

    return -1 if dp[n] == sys.maxsize else dp[n]

if __name__ == "__main__":
    n, x = map(int, input().split())
    print(min_operations(n, x))
