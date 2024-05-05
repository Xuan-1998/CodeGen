def max_similarity_score(A, B):
    max_score = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            for k in range(len(B)):
                for l in range(k + 1, len(B) + 1):
                    score = similarity_score(A[i:j], B[k:l])
                    max_score = max(max_score, score)

    return max_score
