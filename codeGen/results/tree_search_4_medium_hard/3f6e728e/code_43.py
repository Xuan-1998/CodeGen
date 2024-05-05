import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, c = map(int, sys.stdin.readline().split())
        u = list(map(int, sys.stdin.readline().split()))
        l = list(map(int, sys.stdin.readline().split()))

        dp = [[0] * (c + 1) for _ in range(c + 2)]

        dp[0][j] = 1 for all j. Since there are no spheres initially.

        for i in range(1, c + 2):
            for j in range(i, c + 1):
                if i == 1:
                    dp[i][j] = sum(1 if u_k <= j else 0 for k in range(n))
                    dp[i][j] += sum(1 if l_k <= j else 0 for k in range(m))
                else:
                    dp[i][j] = (dp[i - 1][j] * (sum(1 if u_k <= j else 0 for k in range(n)) + 
                                                  sum(1 if l_k <= j else 0 for k in range(m)))) % (10**9 + 7)

        print(*map(str, dp[c]), sep=' ')

if __name__ == "__main__":
    solve()
