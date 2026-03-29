import sys

def lcs_length(a, b):
    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(a, b):
    lcs_len = lcs_length(a, b)
    return 4 * lcs_len - (len(a) + len(b))

def main():
    a = input().strip()
    b = input().strip()

    max_similarity = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            for k in range(len(b)):
                for end in range(k + 1, len(b) + 1):
                    sub_a = a[i:j]
                    sub_b = b[k:end]
                    similarity = similarity_score(sub_a, sub_b)
                    max_similarity = max(max_similarity, similarity)

    print(max_similarity)

if __name__ == "__main__":
    main()
