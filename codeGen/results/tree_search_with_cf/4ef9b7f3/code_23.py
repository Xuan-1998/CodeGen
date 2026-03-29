def can_transform(n, initial_seq, k, final_seq):
    # Initialize the DP table
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(0, k + 1):
            if j > 0 and dp[i - 1][j - 1] and initial_seq[i - 1] == final_seq[j - 1]:
                dp[i][j] = True
            if j > 0 and dp[i - 1][j - 1] and initial_seq[i - 1] > final_seq[j - 1]:
                dp[i][j] = True
            if dp[i - 1][j]:
                dp[i][j] = True

    if not dp[n][k]:
        print("NO")
        return

    # If transformation is possible, reconstruct the operations
    print("YES")
    operations = []
    i, j = n, k

    while i > 0 and j > 0:
        if dp[i][j] and dp[i - 1][j - 1] and initial_seq[i - 1] == final_seq[j - 1]:
            i -= 1
            j -= 1
        elif dp[i][j] and dp[i - 1][j - 1] and initial_seq[i - 1] > final_seq[j - 1]:
            i -= 1
            j -= 1
        elif dp[i][j] and dp[i - 1][j]:
            i -= 1
        else:
            # This should never happen if the DP table is filled correctly
            raise RuntimeError("Unexpected state during backtracking")

    # Output the operations
    for op in reversed(operations):
        print(op)

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

# Call the function
can_transform(n, initial_seq, k, final_seq)

