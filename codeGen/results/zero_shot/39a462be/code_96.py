python
# Step 1: Read input strings A and B
A = input()
B = input()

# Step 2: Initialize maximum similarity score
max_similarity = 0

# Step 3: Iterate over all pairs of substrings in A and B
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for l in range(k + 1, len(B) + 1):
                # Step 4: Calculate the similarity score for the current pair of substrings
                similarity = 4 * longest_common_subsequence(A[i:j], B[k:l]) - (j - i + k - l)
                
                # Step 5: Update maximum similarity score if necessary
                max_similarity = max(max_similarity, similarity)

# Step 6: Print the maximum similarity score
print(max_similarity)
