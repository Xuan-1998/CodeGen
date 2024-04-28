import sys

def solve(n, s):
    # Initialize dp table
    dp = [set() for _ in range(1 << n)]

    # Base case: only one winning team when n = 1
    if n == 1:
        return [int(s[0], 2)]

    # Calculate the winning teams in each round
    for i in range(n):
        for j in range(1 << n):
            # Get the current round's result as a binary string
            curr_s = bin(j)[2:].zfill(n)
            # Get the next round's result by flipping the ith bit
            next_s = curr_s[:i] + ('0' if s[i] == '0' else '1') + curr_s[i+1:]
            # Update dp table based on the current and next rounds' results
            for team in dp[j ^ (1 << i)]:
                if next_s[team] == s[i]:
                    dp[(j | 1) << 1].add(team)
                else:
                    dp[(j | 2) << 1].add(team)

    # Return the winning teams in ascending order
    return sorted(list(set.union(*dp)))

# Read input from stdin and print output to stdout
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(solve(n, s))
