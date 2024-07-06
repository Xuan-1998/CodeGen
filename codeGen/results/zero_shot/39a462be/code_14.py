# Step 1: Read the input strings A and B from standard input
A = input()
B = input()

# Step 2: Initialize the maximum similarity score to 0
max_similarity_score = 0

# Step 3: Iterate over all possible substrings of A and B
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        for k in range(len(B)):
            for l in range(k + 1, len(B) + 1):
                # Step 4: Calculate the LCS of the current substrings
                m = min(j - i, l - k)
                while m > 0 and A[i:i+m] != B[k:k+m]:
                    m -= 1
                
                # Step 5: Calculate the similarity score for the current substrings
                similarity_score = (4 * m) - (j - i + l - k)

                # Step 6: Update the maximum similarity score if necessary
                max_similarity_score = max(max_similarity_score, similarity_score)

# Step 7: Print the maximum similarity score to standard output
print(max_similarity_score)
