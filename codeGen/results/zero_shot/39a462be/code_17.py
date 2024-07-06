# Step 1: Read input strings A and B
A = input()
B = input()

# Step 2: Initialize maximum similarity score
max_similarity_score = 0

# Step 3: Iterate over all possible substrings of A and B
for i in range(len(A)):
    for j in range(i+1, len(A)+1):
        for k in range(len(B)):
            for l in range(k+1, len(B)+1):
                # Step 4: Calculate similarity score for current pair of substrings
                length_A_substring = j - i
                length_B_substring = l - k
                common_subsequence_length = find_LCS(A[i:j], B[k:l]).length
                similarity_score = 4 * common_subsequence_length - (length_A_substring + length_B_substring)
                
                # Step 5: Update maximum similarity score if necessary
                max_similarity_score = max(max_similarity_score, similarity_score)

# Step 6: Print the maximum similarity score
print(max_similarity_score)
