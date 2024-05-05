import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            total_sum = sum([1 if sign == '+' else -1 for k in range(i-1, j)])
            dp[i][j] = min(total_sum // abs(total_sum) * (i-1) + (total_sum % abs(total_sum) != 0), 
                             total_sum // abs(total_sum) * ((n+1)-j) + (total_sum % abs(total_sum) != 0))

    for _ in range(q):
        l, r = map(int, input().split())
        print(dp[l][r])

if __name__ == "__main__":
    solve()
