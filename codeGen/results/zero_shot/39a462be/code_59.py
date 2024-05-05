def lcs_length(s1, s2):
    m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])
    return m[-1][-1]

def similarity_score(s1, s2):
    lcs_len = lcs_length(s1, s2)
    return 4 * lcs_len - len(s1) - len(s2)

A = input().strip()
B = input().strip()
max_similarity = 0
for i in range(len(A)):
    for j in range(i + 1):
        substring_A = A[j:i+1]
        for k in range(len(B)):
            for l in range(k + 1):
                substring_B = B[l:k+1]
                similarity = similarity_score(substring_A, substring_B)
                if similarity > max_similarity:
                    max_similarity = similarity
print(max_similarity)
