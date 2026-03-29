# Step 1: Read input strings A and B from standard input
A = input().strip()
B = input().strip()

# Step 2: Initialize maximum similarity score
max_similarity_score = 0

# Step 3: Iterate over all possible substrings of A and B
for i in range(len(A)):
    for j in range(i + len(A) - len(B) + 1):
        subA = A[i:j]
        for k in range(len(B)):
            for l in range(k + len(B) - len(subA) + 1):
                subB = B[l:l+len(subA)]
                # Step 4: Calculate similarity score for the current pair of substrings
                similarity_score = 4 * len(lcs(subA, subB)) - (len(subA) + len(subB))
                # Step 5: Update maximum similarity score if necessary
                max_similarity_score = max(max_similarity_score, similarity_score)

# Step 6: Print the maximum similarity score to standard output
print(max_similarity_score)
