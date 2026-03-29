import sys

def expected_non_zero_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[[0.0, 0.0] for _ in range(10)] for _ in range(N + 1)]
        
        # Base case: When processing the first digit (n = 0), set dp[0][i][c] to 1 if c is true, and 0 otherwise.
        for i in range(10):
            dp[0][i][True] = 1
            dp[0][i][False] = 0
        
        # Induction step:
        for n in range(N):
            for i in range(10):
                for c in [False, True]:
                    if n > 0 and c:  # If there was a carry from the previous addition
                        for j in range(10):  # Iterate over all possible values of digit at position n
                            dp[n + 1][i][c] += dp[n][j][True] / (10.0 ** N)
                    else:
                        for j in range(10):  # Iterate over all possible values of digit at position n
                            dp[n + 1][i][c] += dp[n][j][c] / (10.0 ** N)
        
        total_pairs = 10 ** N * 10 ** N  # Total number of pairs of N-digit numbers
        non_zero_carries = sum([dp[N][i][True] for i in range(10)])  # Sum the expected non-zero carries for each digit at position N
        
        print(non_zero_carries / total_pairs)  # Print the expected number of non-zero carries

expected_non_zero_carries()
