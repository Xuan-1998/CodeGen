from collections import defaultdict

def solve():
    T = int(input())
    memo = defaultdict(int)

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        res = 0
        for k in range(j + 1):
            if i == 1:
                res += 1
            else:
                res += dp(i - 1, k)
        memo[(i, j)] = res % (10**9 + 7)
        return res

    for _ in range(T):
        N, M = map(int, input().split())
        print(dp(N, M))

if __name__ == "__main__":
    solve()
