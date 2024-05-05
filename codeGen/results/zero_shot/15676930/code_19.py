import sys

def max_total_joy(n):
    # Read input from stdin
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(3)]

    for i in range(n):
        if i == 0:
            dp[0][i+1] = a[i]
            dp[1][i+1] = b[i]
            dp[2][i+1] = c[i]
        else:
            dp[0][i+1] = max(dp[1][i]+a[i], dp[0][i-1]+b[i])
            dp[1][i+1] = max(dp[2][i-1]+c[i], dp[1][i-1]+b[i])
            dp[2][i+1] = dp[2][i]

    # Print the maximum total joy to stdout
    print(max(dp[0][-1], dp[1][-1], dp[2][-1]))

if __name__ == "__main__":
    n = int(input())
    max_total_joy(n)
