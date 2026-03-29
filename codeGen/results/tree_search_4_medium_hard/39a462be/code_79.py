import sys

def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    memo = {(i, j): None for i in range(n + 1) for j in range(m + 1)}

    def lcs(i, j):
        if memo[(i, j)] is not None:
            return memo[(i, j)]

        if i == 0 or j == 0:
            memo[(i, j)] = min(i, j) - 4 * max(i, j)
        else:
            k = min(i, j)
            while k > 0 and a[i - k] == b[j - k]:
                k -= 1
            dp[i][j] = lcs(i - 1, j - 1) + 4 * k - i - j
            memo[(i, j)] = dp[i][j]

        return dp[i][j]

    max_similarity = 0
    for i in range(n + 1):
        for j in range(m + 1):
            similarity = lcs(i, j)
            if similarity > max_similarity:
                max_similarity = similarity

    print(max_similarity)

if __name__ == "__main__":
    solve()
