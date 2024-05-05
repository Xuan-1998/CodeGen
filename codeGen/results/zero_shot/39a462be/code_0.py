import sys

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
    lcs_length_val = lcs_length(s1, s2)
    return 4 * lcs_length_val - len(s1) - len(s2)

# Read input from stdin
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

# Calculate the maximum similarity score over all pairs of substrings
max_similarity_score = 0
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        sub_A = A[i:j]
        for k in range(len(B)):
            for end in range(k + 1, len(B) + 1):
                sub_B = B[k:end]
                similarity_score_val = similarity_score(sub_A, sub_B)
                if similarity_score_val > max_similarity_score:
                    max_similarity_score = similarity_score_val

# Print the result to stdout
print(max_similarity_score)
