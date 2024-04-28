import sys

def solve(n, s):
    # Initialize the result array
    res = []

    def dfs(mask, team_id=0):
        nonlocal res
        # Convert the mask to binary and remove the '0b' prefix
        bin_mask = bin(mask)[2:]

        # If the length of the binary string is equal to n, it's a winning team
        if len(bin_mask) == n:
            res.append((team_id, int(bin_mask, 2)))

        for i in range(n):
            # Calculate the new mask by flipping the ith bit
            new_mask = (mask | (1 << i)) & ((1 << (n - i)) - 1)
            dfs(new_mask, team_id | (1 << i))

    dfs(0)

    res.sort()
    for winning_team in res:
        print(winning_team[0])
