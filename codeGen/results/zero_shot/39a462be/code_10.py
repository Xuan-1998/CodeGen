import sys

# Read input strings A and B
A = input().strip()
B = input().strip()

# Initialize maximum similarity score
max_similarity_score = 0

# Iterate over all pairs of substrings of A and B
for i in range(len(A)):
    for j in range(min(i+1, len(A)-i), min(j+1, len(B)-j)+1):
        for k in range(len(A) - i + 1):
            if A[i:i+k] == B[j:j+k]:
                # Calculate similarity score for current pair of substrings
                similarity_score = 4 * k - (i + k)
                max_similarity_score = max(max_similarity_score, similarity_score)

# Print maximum similarity score
print(max_similarity_score)
