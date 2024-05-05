import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n+1) for _ in range(n+1)]
    prefix_sum = [0]
    total_signs = 0

    for i in range(n):
        if signs[i] == '+':
            total_signs += 1
        else:
            total_signs -= 1
        prefix_sum.append(prefix_sum[-1] + (1 if signs[i] == '+' else -1))

    for l in range(1, n+1):
        for r in range(l, n+1):
            if prefix_sum[r] - prefix_sum[l-1] == 0:
                dp[l][r] = 0
            else:
                min_remove = float('inf')
                for i in range(l, r+1):
                    if (prefix_sum[i] - prefix_sum[l-1]) % 2 != 0:
                        min_remove = min(min_remove, dp[l][i-1] + dp[i+1][r] + 1)
                dp[l][r] = min_remove

    for _ in range(q):
        l, r = map(int, input().split())
        print(dp[l][r])

if __name__ == "__main__":
    solve()
