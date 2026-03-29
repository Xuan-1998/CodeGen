import sys

def is_ladder(arr):
    n = len(arr)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if arr[j - 1] <= arr[j]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = (dp[i][j - 1] or dp[i][j - 1])

    return dp

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = []
    for _ in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))

    dp = is_ladder(arr)

    for query in queries:
        l, r = query
        if dp[l][r]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
