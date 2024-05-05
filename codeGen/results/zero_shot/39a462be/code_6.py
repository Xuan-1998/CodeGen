def calculate_similarity_score(a, b):
    lcs_length = find_lcs(a, b)
    m = len(a)
    n = len(b)
    return 4 * lcs_length - (m + n)

# Read input strings A and B
a = input()
b = input()

# Calculate the similarity score
score = calculate_similarity_score(a, b)

print(score)  # Print the result
