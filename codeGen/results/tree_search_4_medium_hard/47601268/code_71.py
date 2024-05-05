from sys import stdin

def solve():
    n = int(stdin.readline())
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        last_bit = (i & 1) == 1
        if not last_bit or all((i >> j) & 1 != (i >> (j - 1)) & 1 for j in range(i.bit_length())):
            dp[i] = 1 + (dp[i - 1] if i > 0 else 0)
    print(sum(dp))

if __name__ == "__main__":
    solve()
