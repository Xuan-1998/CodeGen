def similarity_score(i, j):
    if i == len(A) or j == len(B):  # base case: no more common characters to find
        return (k * 4 - (i + j))  # calculate the maximum similarity score

    if memo.get((i, j)):
        return memo[(i, j)]  # retrieve cached result

    char_match = A[i] == B[j]
    if char_match:
        k += 1
        next_i, next_j, next_k = i + 1, j + 1, k
    else:
        k = 0
        next_i, next_j = i + 1, j + 1

    result = similarity_score(next_i, next_j)
    memo[(i, j)] = result  # store intermediate result for future reference

    return result

A, B = input().split()
n, m = len(A), len(B)

memo = {}
max_similarity_score = 0
for i in range(n):
    for j in range(m):
        max_similarity_score = max(max_similarity_score, similarity_score(i, j))

print(max_similarity_score)
