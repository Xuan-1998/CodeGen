import sys

def compute_similarity_score(a, b):
    n = len(a)
    m = len(b)

    # Generate all possible substrings
    substrings_a = [[a[i:j] for j in range(i+1, n+1)] for i in range(n)]
    substrings_b = [[b[i:j] for j in range(i+1, m+1)] for i in range(m)]

    max_similarity_score = 0

    # Compute the LCS and similarity score for each pair of substrings
    for substring_a in substrings_a:
        for substring_b in substrings_b:
            lcs_length = 0
            for char_a in substring_a[0]:
                for char_b in substring_b[0]:
                    if char_a == char_b:
                        lcs_length += 1
                        break
                else:
                    continue
                break
            similarity_score = 4 * lcs_length - (len(substring_a) + len(substring_b))
            max_similarity_score = max(max_similarity_score, similarity_score)

    return max_similarity_score

# Read input from stdin
a = input().strip()
b = input().strip()

# Compute and print the maximum similarity score
max_similarity_score = compute_similarity_score(a, b)
print(max_similarity_score)
