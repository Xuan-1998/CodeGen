# Step 1: Read input strings
A = input().strip()
B = input().strip()

# Step 2: Initialize maximum similarity score
max_similarity = -float('inf')

# Step 3: Iterate over all possible substrings of A and B
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for l in range(k + 1, len(B) + 1):
                # Step 4: Calculate the length of LCS for current substrings
                lcs_len = find_lcs_length(A[i:j], B[k:l])

                # Step 5: Calculate the similarity score for current substrings
                similarity = 4 * lcs_len - (j - i + k - l)

                # Step 6: Update maximum similarity score if necessary
                max_similarity = max(max_similarity, similarity)

print(max_similarity)
