from collections import defaultdict

A = input().strip()
B = input().strip()

max_similarity_score = -1

def LCS(substring_A, substring_B):
    m = len(substring_A)
    n = len(substring_B)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if substring_A[i-1] == substring_B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

for i in range(len(A)):
    for j in range(i+1, len(A)+1):
        substring_A = A[i:j]

    for k in range(len(B)):
        for l in range(k+1, len(B)+1):
            substring_B = B[k:l]
            
            similarity_score = 4*LCS(substring_A, substring_B) - len(substring_A) - len(substring_B)
            if similarity_score > max_similarity_score:
                max_similarity_score = similarity_score

print(max_similarity_score)
