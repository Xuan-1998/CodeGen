# Read input strings
A = input()
B = input()

# Initialize maximum similarity score
max_similarity_score = 0

# Iterate over all possible substrings of A and B
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for end_k in range(k + 1, len(B) + 1):
                # Calculate the similarity score for the current pair of substrings
                lcs_length = 0
                for p in range(i, j):
                    if A[p] == B[k]:
                        k += 1
                        lcs_length += 1

                if lcs_length > max_similarity_score:
                    max_similarity_score = lcs_length * 4 - (j - i + end_k - k)

# Print the maximum similarity score
print(max_similarity_score)
