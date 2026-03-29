def similarity_score(C, D):
    lcs = find_lcs(C, D)
    return 4 * len(lcs) - (len(C) + len(D))

def find_lcs(C, D):
    m = len(C)
    n = len(D)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if C[i - 1] == D[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if C[i - 1] == D[j - 1]:
            lcs.append(C[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

def max_similarity_score(A, B):
    max_score = 0
    for i in range(len(A) + 1):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B) + 1):
                for l in range(k + 1, len(B) + 1):
                    score = similarity_score(A[i:j], B[k:l])
                    max_score = max(max_score, score)
    return max_score

if __name__ == '__main__':
    A = input().strip()
    B = input().strip()
    print(max_similarity_score(A, B))
