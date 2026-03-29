import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i + 1):
                c = a[j - 1] * j + s * (i - j)
                if c < dp[i]:
                    dp[i] = c
        print(dp[-1])

if __name__ == "__main__":
    solve()
