from collections import defaultdict

def max_similarity_score():
    n, m = map(int, input().split())
    a = input()
    b = input()

    dp = [[defaultdict(int) for _ in range(m+1)] for _ in range(n+1)]
    memo = {}

    def lcs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 or j == 0:
            return ''
        if a[i-1] == b[j-1]:
            result = f"{a[i-1]}{lcs(i-1, j-1)}"
        else:
            result = lcs(i-1, j) if i > 0 and dp[i-1][j].get(0, 0) < len(result) else lcs(i, j-1) if j > 0 and dp[i][j-1].get(0, 0) < len(result) else ''
        memo[(i, j)] = result
        return result

    for i in range(n+1):
        for j in range(m+1):
            lcs_len = len(lcs(i, j))
            dp[i][j] = {k: v for k, v in enumerate(f"{a[:i]}{b[:j]}"[:lcs_len], 0)}
    max_score = 0
    for i in range(n+1):
        for j in range(m+1):
            if dp[i].get(j, 0) > 0:
                lcs_len = len(lcs(i, j))
                score = 4 * lcs_len - (i + j)
                max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    max_similarity_score()
