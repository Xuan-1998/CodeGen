dp = {(0, 0): 0}  # dp[(i, j)] represents the similarity score up to indices i in A and j in B
max_similarity = 0

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[(i+1, j+1)] = dp.get((i, j), 0) + 4  # increment by 4 when characters match
        else:
            dp[(i+1, j)] = max(dp.get((i, j), 0), dp.get((i+1, j-1), 0)) if j > 0 else max(dp.get((i, j), 0), 0)
        max_similarity = max(max_similarity, dp[(i+1, j)])

print(max_similarity - (len(A) + len(B)))
