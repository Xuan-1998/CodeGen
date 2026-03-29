import sys

def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(s1, s2):
    lcs_len = lcs_length(s1, s2)
    return 4 * lcs_len - (len(s1) + len(s2))

def main():
    A, B = input().split(), input().split()
    max_similarity = 0

    for i in range(len(A)):
        for j in range(i, len(A)):
            for k in range(len(B)):
                for end in range(k, len(B)):
                    score = similarity_score(''.join(A[i:j+1]), ''.join(B[k:end+1]))
                    max_similarity = max(max_similarity, score)

    print(max_similarity)

if __name__ == '__main__':
    main()
