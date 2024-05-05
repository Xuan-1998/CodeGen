# Initialize the maximum similarity score as negative infinity
max_similarity = float('-inf')

# Iterate over all possible substrings of string A
for i in range(len(A)):
    # Iterate over all possible substrings of string B
    for j in range(len(B)):
        # Initialize the number of common characters found so far to 0
        k = 0
        
        # Compare the current substring of string A with the current substring of string B
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                # If the characters match, increment the number of common characters found so far
                k += 1
                # Move to the next character in both strings
                i += 1
                j += 1
            elif i < len(A) - 1:
                # If the characters don't match and there are more characters left in string A, move to the next character
                i += 1
            else:
                break
            elif j < len(B) - 1:
                # If the characters don't match and there are more characters left in string B, move to the next character
                j += 1
            else:
                break
        
        # Calculate the maximum similarity score for the current substrings
        max_similarity = max(max_similarity, k * 4 - i - j)

# Print the maximum similarity score
print(max_similarity)
