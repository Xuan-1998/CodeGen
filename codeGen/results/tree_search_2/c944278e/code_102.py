def find_winners(n):
    # Create a 2D array to store the dynamic programming results
    dp = [[[] for _ in range(2**n)] for _ in range(n)]

    # Base case: when the phase reaches its maximum value (2^n - 1), 
    # there's only one winning team, which is the last remaining team.
    for i in range(n):
        dp[i][2**n - 1] = [str(i + 1)]

    # Fill up the dynamic programming table using the optimal substructure
    for i in range(n-1, -1, -1):
        for j in range(2**i - 1, -1, -1):
            if not dp[i][j]:
                continue
            winners = dp[i][j]
            for winner in winners:
                # Determine the winning team(s) at phase i+1
                next_winners = []
                for k in range(j + 1, 2**i):
                    if str(int(winner) ^ int(str(k))) not in winners:
                        next_winners.append(str(int(winner) ^ int(str(k))))
                dp[i+1][j] = next_winners

    # Return the winning teams at phase 0
    return dp[0][0]

# Read input from stdin
n = int(input())
s = input()

# Call the find_winners function and print the result to stdout
print(find_winners(n))
