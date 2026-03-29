import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [1] + [0] * (n + 1)
        for i in range(1, n + 1):
            and_val = 2 ** k - 1
            xor_val = 0
            for j in range(i):
                x = int(input())
                and_val &= x
                xor_val ^= x
            dp[i] = (dp[i - 1] * ((and_val >= xor_val) + 1)) % (10 ** 9 + 7)
        print(dp[n])

if __name__ == "__main__":
    solve()
