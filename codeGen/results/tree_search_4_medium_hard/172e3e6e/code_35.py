import sys

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    max_val = max(a)
    dp = [[False] * (max_val + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        for d in range(1, max_val+1):
            if a[i-1] % d == 0:
                if i == 1 or dp[i-1][d]:
                    dp[i][d] = True

    ans = sum(dp[i][max(a)] for i in range(n+1))
    print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
