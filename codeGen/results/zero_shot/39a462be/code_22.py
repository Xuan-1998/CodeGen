import sys

def lcs_length(X , Y):
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(X , Y):
    lcs_len = lcs_length(X, Y)
    return 4 * lcs_len - (len(X) + len(Y))

def main():
    a = input().strip()
    b = input().strip()

    max_similarity = 0
    for i in range(len(a)):
        for j in range(i + 1):
            substr_a = a[j:i+1]
            for k in range(len(b)):
                for l in range(k + 1):
                    substr_b = b[l:k+1]
                    similarity = similarity_score(substr_a, substr_b)
                    max_similarity = max(max_similarity, similarity)

    print(max_similarity)

if __name__ == "__main__":
    main()
