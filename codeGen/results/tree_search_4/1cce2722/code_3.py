def maxPoints(a):
    n = len(a)
    dp = [[0] * n for _ in range(n)]

    # Base case: For a sequence of length 1 or 2, the maximum number of points is the number of elements.
    for i in range(2):
        dp[i][i] = 1

    # Fill up the DP table by considering all possible subproblems.
    for len_subseq in range(3, n + 1):
        for i in range(n - len_subseq + 1):
            j = i + len_subseq - 1
            if a[i] == a[j]:
                dp[i][j] = max(dp[i+1][j-1], 1) if j > i + 1 else 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + 1

    # The final answer is the maximum number of points that can be earned by deleting elements up to index n.
    return dp[0][n - 1]

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

print(maxPoints(a))
