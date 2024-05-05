def lcs_length(X , Y):
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    longest, x_longest = 0, 0

    for mm in range(1, m + 1):
        for nn in range(1, n + 1):

            if X[mm - 1] == Y[nn - 1]:
                dp[mm][nn] = dp[mm - 1][nn - 1] + 1

                if dp[mm][nn] > longest:
                    longest = dp[mm][nn]
                    x_longest = mm
            else:
                dp[mm][nn] = max(dp[mm - 1][nn], dp[mm][nn - 1])

    return longest


def find_max_similarity_score(A, B):
    max_similarity = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):

            for k in range(len(B)):
                for end in range(k + 1, len(B) + 1):
                    lcs_length_A_B = lcs_length(A[i:j], B[k:end])
                    similarity_score = (4 * lcs_length_A_B) - (j - i + end - k)
                    if similarity_score > max_similarity:
                        max_similarity = similarity_score

    return max_similarity


def main():
    A = input()
    B = input()

    print(find_max_similarity_score(A, B))


if __name__ == "__main__":
    main()
