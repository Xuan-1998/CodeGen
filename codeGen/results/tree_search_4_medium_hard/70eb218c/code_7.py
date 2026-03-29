from sys import stdin

def min_operations(x, n):
    dp = [[-1] * (n + 1) for _ in range(10**(n-1))]

    def dfs(i):
        if i < 0 or i >= len(dp[0]):
            return -1
        if n == 1:
            return 0
        if x % 10 != 0 and dp[x][n] != -1:
            return dp[x][n]
        if x % 10 == 0:
            return dfs(int(x / 10)) + 1
        else:
            for d in range(10):
                if (x * 10 + d) % 10**n == 0 and dp[int(x*10+d)][n-1] != -1:
                    return min(dfs(int(x*10+d)), dp[x][n]) + 1
        return -1

    return dfs(int(x))

if __name__ == "__main__":
    n, x = map(int, stdin.readline().split())
    print(min_operations(x, n))
