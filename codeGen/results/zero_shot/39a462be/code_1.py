# Step 1: Read input strings A and B
A = input().strip()
B = input().strip()

# Step 2: Initialize variables to store maximum similarity score and its corresponding substrings
max_similarity_score = 0
substring_A = ""
substring_B = ""

# Step 3: Iterate over all possible pairs of substrings from A and B
for i in range(len(A)):
    for j in range(i + 1, len(A) + 1):
        substring_A = A[i:j]
        
        for k in range(len(B)):
            for l in range(k + 1, len(B) + 1):
                substring_B = B[k:l]
                
                # Step 4: Calculate the similarity score of the current pair of substrings
                similarity_score = 4 * len(lcs(substring_A, substring_B)) - (len(substring_A) + len(substring_B))
                
                if similarity_score > max_similarity_score:
                    max_similarity_score = similarity_score
                    substring_A = substring_A
                    substring_B = substring_B

# Step 5: Print the maximum similarity score and its corresponding substrings
print(max_similarity_score)
