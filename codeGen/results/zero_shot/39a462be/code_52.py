python
n, m = map(int, input().split())
A = input().strip()
B = input().strip()
max_similarity = 0

for i in range(n):
    for j in range(i+1, n+1):
        substr_A = A[i:j]
        for k in range(m):
            for l in range(k+1, m+1):
                substr_B = B[k:l]
                lcs_length = [[0] * (l + 1) for _ in range(j + 1)]
                for x in range(1, j + 1):
                    for y in range(1, l + 1):
                        if substr_A[x - 1] == substr_B[y - 1]:
                            lcs_length[x][y] = lcs_length[x - 1][y - 1] + 1
                        else:
                            lcs_length[x][y] = max(lcs_length[x - 1][y], lcs_length[x][y - 1])
                similarity_score = 4 * lcs_length[j][l] - (j + k)
                max_similarity = max(max_similarity, similarity_score)

print(max_similarity)
