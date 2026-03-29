def similarity(A, B):
    LCS_length = 0
    
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    LCS_length = dp[-1][-1]
    A_length, B_length = len(A), len(B)
    score = 4 * LCS_length - (A_length + B_length)
    
    return score

def max_similarity(A, B):
    max_score = -1
    
    for i in range(1, min(len(A), len(B)) + 1):
        A_substrings = [A[j:j+i] for j in range(len(A) - i + 1)]
        B_substrings = [B[j:j+i] for j in range(len(B) - i + 1)]
        
        scores = [(similarity(sub_A, sub_B), sub_A, sub_B)
                   for sub_A in A_substrings
                   for sub_B in B_substrings]
        
        max_score = max(max_score, max(score[0] for score in scores))
    
    return max_score

if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    
    max_score = max_similarity(A, B)
    
    print(max_score)
