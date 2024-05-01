def findShortestSubSequence(input1, input2):
    m = len(input1)
    n = len(input2)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    shortest_length = float('inf')

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if input1[i - 1] == input2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = (dp[i - 1][j] or
                            dp[i][j - 1])

            if not dp[i][j] and i == j:
                shortest_length = min(shortest_length, i)

    return -1 if shortest_length == float('inf') else m - shortest_length


# Read input from stdin
S = input()
T = input()

print(findShortestSubSequence(S, T))
