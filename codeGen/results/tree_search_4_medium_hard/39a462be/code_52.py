def max_similarity_score():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)
    memo = {(0, 0): 0}

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                k = memo.get((i - 1, j - 1), 0) + 1
                memo[(i, j)] = max(4 * k - i - j, memo.get((i - 1, j), 0) + memo.get((i, j - 1), 0))
            else:
                memo[(i, j)] = max(memo.get((i - 1, j), 0), memo.get((i, j - 1), 0))

    return memo.get((n, m), 0)

print(max_similarity_score())
