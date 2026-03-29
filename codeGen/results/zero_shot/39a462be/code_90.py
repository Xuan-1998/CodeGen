def similarity_score(A, B):
    lcs_len = lcs_length(A, B)
    sum_length = len(A) + len(B)
    return 4 * lcs_len - sum_length

# Read input from stdin
A = input().strip()
B = input().strip()

# Calculate and print the similarity score to stdout
print(similarity_score(A, B))
