import sys

def solve():
    n, x = map(int, input().split())
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        if len(str(x)) < i - 1:
            dp[i] = dp[i - 1] + 1
        else:
            min_ops = sys.maxsize
            for j in range(i - 1, 0, -1):
                ops = dp[j - 1] + (i - j - 1) + (int(str(x)[j:]) != 0)
                if ops < min_ops:
                    min_ops = ops
            dp[i] = min_ops

    print(dp[n])

if __name__ == "__main__":
    solve()
