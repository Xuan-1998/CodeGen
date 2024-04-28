def findShortestSubArray(S: str, T: str) -> int:
    # Find the longest common subsequence (LCS) in S and T
    m = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])
    
    # Find the LCS in each string separately
    lcs_S = [[0] * (len(S) + 1) for _ in range(len(S) + 1)]
    lcs_T = [[0] * (len(T) + 1) for _ in range(len(T) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(S) + 1):
            if S[i - 1] == S[j - 1]:
                lcs_S[i][j] = lcs_S[i - 1][j - 1] + 1
            else:
                lcs_S[i][j] = max(lcs_S[i - 1][j], lcs_S[i][j - 1])
    for i in range(1, len(T) + 1):
        for j in range(1, len(T) + 1):
            if T[i - 1] == T[j - 1]:
                lcs_T[i][j] = lcs_T[i - 1][j - 1] + 1
            else:
                lcs_T[i][j] = max(lcs_T[i - 1][j], lcs_T[i][j - 1])
    
    # Calculate the length of the shortest uncommon subsequence
    return min(m[-1][-1], lcs_S[-1][-1], lcs_T[-1][-1]) - 1

S = input().strip()
T = input().strip()

print(findShortestSubArray(S, T))
