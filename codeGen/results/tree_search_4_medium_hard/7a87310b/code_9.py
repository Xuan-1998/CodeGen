import sys

def dp(i, j):
    if i == 0 and j == 0:
        return 1
    elif i < 3 or j < 3:
        return 0
    else:
        ans = 0
        for k in range(min(i, j)+1):
            ans += dp[i-k][j-k]
        return ans

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        ans = 0
        for i in range(3, N+1):
            for j in range(i, N+1):
                if (i + j) % 2 == 1:  # only consider matrices with odd trace
                    ans += dp(i, j)
        print(ans)

if __name__ == "__main__":
    solve()
