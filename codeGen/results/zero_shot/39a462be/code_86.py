A = input().strip()
B = input().strip()

def generate_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return substrings

A_substrs = generate_substrings(A)
B_substrs = generate_substrings(B)

def calculate_similarity_score(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs_length = dp[m][n]
    return 4 * lcs_length - (m + n)

max_similarity_score = 0

for s1 in A_substrs:
    for s2 in B_substrs:
        similarity_score = calculate_similarity_score(s1, s2)
        max_similarity_score = max(max_similarity_score, similarity_score)

print(max_similarity_score)
