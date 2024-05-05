def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    dp = [[[False] * (10**9 + 1) for _ in range(k + 1)] for _ in range(n)]

    for i in range(n):
        mi = mx = values[i]
        for j in range(min(i, k), -1, -1):
            if all((mi ^ values[j]) == (mx ^ values[j]) for j in range(i)):
                dp[i][j][mi ^ values[i]] = True

    return "YES" if any(dp[-1][-1][k]) else "NO"


if __name__ == "__main__":
    while True:
        try:
            print(solve())
        except ValueError:
            break
