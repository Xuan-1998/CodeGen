def lcs_length(X , Y):
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for t in range(m + 1):
        for s in range(n + 1):
            if t == 0:
                L[t][s] = s
            elif s == 0:
                L[t][s] = t
            elif X[t - 1] == Y[s - 1]:
                L[t][s] = L[t - 1][s - 1] + 1
            else:
                L[t][s] = max(L[t - 1][s], L[t][s - 1])

    return L[m][n]

def similarity_score(A, B):
    return 4 * lcs_length(A, B) - (len(A) + len(B))

A = input().strip()
B = input().strip()

print(similarity_score(A, B))
