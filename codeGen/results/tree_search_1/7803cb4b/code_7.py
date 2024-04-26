def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def solve(n, a):
    # Initialize the DP table with a large number
    dp = [[[float('inf')] * (n + 1) for _ in range(n)] for _ in range(n)]

    # Base case: subarrays of length 1
    for i in range(n):
        dp[i][i][a[i]] = 1

    # Fill the DP table for subarrays of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(1, 1001):
                # Case 1: If the ends can be combined
                if a[i] == a[j] and a[i] == k - 1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i + 1][j - 1][k])

                # Case 2: Partition the subarray and combine the results
                for m in range(i, j):
                    dp[i][j][k] = min(dp[i][j][k], dp[i][m][k] + dp[m + 1][j][k])

    # Find the minimum possible length for the entire array
    answer = min(dp[0][n - 1])
    return answer

def main():
    n, a = read_input()
    answer = solve(n, a)
    print(answer)

if __name__ == "__main__":
    main()
