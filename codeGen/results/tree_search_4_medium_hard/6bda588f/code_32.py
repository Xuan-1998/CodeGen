import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + (a[i - 1] - s) * ((a[i - 1] - s) >= 0), 
                        dp[i - 2] + prefix_sum[i] - prefix_sum[i - 2])

        print(min(dp))

if __name__ == "__main__":
    solve()
