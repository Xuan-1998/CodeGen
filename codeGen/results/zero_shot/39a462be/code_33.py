import sys

def lcs_length(A, B):
    # Calculate the length of the longest common subsequence using dynamic programming
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def similarity_score(A, B):
    # Calculate the numerator part of the similarity score
    lcs_length_A_B = lcs_length(A, B)
    lcs_length_B_A = lcs_length(B, A)
    max_similarity_numerator = 4 * min(lcs_length_A_B, lcs_length_B_A)
    
    # Calculate the denominator part of the similarity score
    total_length = len(A) + len(B)
    
    # Calculate the similarity score
    similarity_score = max_similarity_numerator - total_length
    
    return similarity_score

def main():
    A = input().strip()
    B = input().strip()
    
    max_similarity = float('-inf')
    
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            substring_A = A[i:j]
            for k in range(len(B)):
                for end_k in range(k + 1, len(B) + 1):
                    substring_B = B[k:end_k]
                    
                    # Calculate the similarity score for this pair of substrings
                    similarity = similarity_score(substring_A, substring_B)
                    
                    # Update the maximum similarity score if needed
                    max_similarity = max(max_similarity, similarity)
    
    print(max_similarity)

if __name__ == '__main__':
    main()
