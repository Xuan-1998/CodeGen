python
# Step 1: Understand the problem statement
print("The problem is to find the maximal similarity score over all pairs of substrings.")

# Step 2: Define what the similarity score is
def similarity_score(a, b):
    # The similarity score is defined as 4 times the length of the longest common subsequence minus the sum of lengths
    lcs = find_lcs(a, b)
    return 4 * len(lcs) - (len(a) + len(b))

# Step 3: Define a function to find the longest common subsequence
def find_lcs(a, b):
    # Initialize a 2D table to store lengths of LCS
    m = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Fill the table
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    # The LCS is the sequence of characters at the end of the table
    lcs = []
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        elif m[i - 1][j] > m[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the LCS since we built it backwards
    lcs.reverse()

    return "".join(lcs)

# Step 4: Read input and calculate the maximal similarity score
a = input().strip()
b = input().strip()
max_similarity_score = 0
for i in range(len(a)):
    for j in range(i + 1):
        # Calculate the similarity score for the substring from index i to i + len(b) - j
        max_similarity_score = max(max_similarity_score, similarity_score(a[i:i + len(b) - j], b))
print(max_similarity_score)
