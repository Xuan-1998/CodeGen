import sys

def dp(i, j, k):
    if i == 0 or j == 0:
        return 4 * k - (i + j)
    
    max_score = 0
    
    for x in range(1, i+1):
        for y in range(1, j+1):
            if A[x-1:i] == B[y-1:j]:
                new_k = k + 1
                score = dp(x-1, j-1, new_k)
                max_score = max(max_score, score)
    
    return max_score

n, m = map(int, input().split())
A = input().strip()
B = input().strip()

dp_table = [[0] * (m+1) for _ in range(n+1)]
max_similarity = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        dp_table[i][j] = dp(i, j, 0)
        max_similarity = max(max_similarity, dp_table[i][j])

print(max_similarity)
