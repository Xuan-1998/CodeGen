import sys

def solve():
    n = int(sys.stdin.readline().strip())
    s = list(map(int, sys.stdin.readline().strip()))

    # Create a 2D table dp where dp[i][j] represents the set of winning teams for the first i phases when the number of teams is 2^j.
    dp = [[] for _ in range(n + 1)]

    # Initialize the base case: dp[0][i] = [] for all i. This means that when there are no teams (n=0), there are no winning teams.
    for i in range(18):
        dp[0].append([])

    # Fill in the table recursively
    for i in range(n + 1):
        for j in range(1, min(i + 1, 18) + 1):
            if i < j:
                dp[i].append([])
            else:
                temp = set()
                for k in range(2**j):
                    bit_count = bin(k).count('1')
                    if (s[j - 1] and bit_count % 2 == 0) or ((not s[j - 1]) and bit_count % 2 != 0):
                        temp.update(dp[i - j][bit_count])
                dp[i].append(list(temp))

    # Print out the set of winning teams for the last row (dp[n][18]) in ascending order
    print(' '.join(map(str, sorted(set().union(*dp[n])))))

if __name__ == "__main__":
    solve()
