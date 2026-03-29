def lcs_length(X , Y):
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                L[i][j] = j
            elif j == 0:
                L[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = min(L[i - 1][j], L[i][j - 1])

    return L[m][n]

def calculate_similarity_score(A, B):
    n = len(A)
    m = len(B)

    max_score = 0

    for i in range(n + 1):
        for j in range(m + 1):
            k = min(i, j)
            substr_A = A[i - k:i]
            substr_B = B[j - k:j]

            score = 4 * lcs_length(substr_A, substr_B) - (i + j)

            max_score = max(max_score, score)

    return max_score

A = input().strip()
B = input().strip()

print(calculate_similarity_score(A, B))
