import sys
from math import floor

def solve():
    n = int(input())
    t = int(input())
    dec_fraction = float(input())

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        time_taken = len(str(dec_fraction).split('.')[1].replace('0', '')) - floor(i / 3.16) if dec_fraction >= 5 else len(str(dec_fraction).split('.')[1])
        dp[i] = min(dp[i-1], dp[max(0, i-1)] + (dec_fraction * 10 ** (i % 1000)).floor())

    print(int(min(max(dp), t)))

if __name__ == "__main__":
    solve()
