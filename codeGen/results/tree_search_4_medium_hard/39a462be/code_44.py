def similarity(A, B):
    dp = [[[(0, 0, 0)] for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1][2] + 1, i, j)
            else:
                dp[i][j] = max((dp[i - 1][j][2], i, j), key=lambda x: (4 * x[2] - len(A) - len(B)))
    
    max_similarity_score = 0
    for k in range(len(A)):
        for l in range(len(B)):
            if dp[k + 1][l + 1][2] > max_similarity_score:
                max_similarity_score = dp[k + 1][l + 1][2]
    
    return 4 * max_similarity_score - len(A) - len(B)

# read input from stdin
A = input()
B = input()

print(similarity(A, B))
