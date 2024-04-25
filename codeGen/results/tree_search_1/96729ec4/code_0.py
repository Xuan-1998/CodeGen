import sys

def count_square_submatrices(matrix, n, m):
    dp = [[0] * m for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                if i == 0 or j == 0 or j < i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            total += dp[i][j]

    return total

def main():
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(sys.stdin.readline().strip()) for _ in range(n)]
    result = count_square_submatrices(matrix, n, m)
    print(result)

if __name__ == "__main__":
    main()
