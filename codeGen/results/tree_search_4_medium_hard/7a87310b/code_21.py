from collections import Counter

def count_positive_invertible_matrices(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Trivial case: when i = N, there's only one way to construct a PIIM with trace N
    dp[0][n] = 1

    for i in range(3, n + 1):
        for j in range(1, i + 1):
            if j == 1:
                # If the top-left element is 1, we can construct a PIIM with trace i and determinant j
                dp[i][j] = dp[0][i - 1]
            else:
                # Otherwise, we need to count the number of PIIMs with trace i - j and determinant j
                dp[i][j] = dp[0][i - j]

    # Count the total number of PIIMs with trace N and positive determinant
    return sum(dp[-1])

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(count_positive_invertible_matrices(n))

if __name__ == "__main__":
    main()
