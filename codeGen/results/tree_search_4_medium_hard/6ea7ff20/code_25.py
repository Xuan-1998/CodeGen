def solve():
    n = int(input())  # Read n from input
    p = list(map(int, input().split()))  # Read permutation p

    dp = [[False] * (n + 1) for _ in range(n + 1)]  # Initialize DP table
    dp[0][0] = True  # Base case: empty arrays can be merged to form an empty permutation

    for i in range(n):
        for j in range(min(i, n - i)):
            if p[2 * i + j] < p[2 * i + j + 1]:  # Transition relationship 1
                dp[i][j] = dp[i][0] and a[:i].can_be_merged_with(b[:j])
            elif p[2 * i + j] == p[-1]:  # Transition relationship 2
                dp[i][j] = True
            else:
                dp[i][j] = False

    if dp[n - 1][0]:
        print("YES")
    else:
        print("NO")

# Helper function to check if array a[:i] can be merged with b[:j]
def can_be_merged_with(a, j):
    # Implement this function based on your intuition
    pass

if __name__ == "__main__":
    solve()
