import sys

def solve():
    n, t = map(int, input().split())
    fractional_part = float(input())

    dp = [0] * (n + 1)
    for i in range(n, -1, -1):
        if i > 0:
            rounded_value = int(fractional_part * 10**i) / 10**i
            dp[i] = max(dp[i-1], min(rounded_value, t))
        else:
            dp[0] = fractional_part

    return str(int(max(dp)))

if __name__ == "__main__":
    print(solve())
