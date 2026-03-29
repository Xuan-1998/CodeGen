def read_input():
    A = input().strip()
    B = input().strip()
    return A, B

def calculate_similarity(A, B):
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_similarity = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_similarity = max(max_similarity, 4 * dp[i][j] - i - j)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return max_similarity

def main():
    A, B = read_input()
    print(calculate_similarity(A, B))

if __name__ == "__main__":
    main()
