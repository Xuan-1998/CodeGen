def is_ladder_query(array, l, r):
    n = len(array)
    dp = [[False] * (r + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(l, r + 1):
            if array[i-1] <= array[j]:
                dp[i][j] = any(dp[i-1][k] for k in range(j))
            elif array[i-1] >= array[j]:
                dp[i][j] = any(dp[i-1][k] for k in range(l, j))

    return "Yes" if dp[n][r] else "No"

def main():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    queries = []
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))

    for query in queries:
        print(is_ladder_query(array, query[0], query[1]))

if __name__ == "__main__":
    main()
