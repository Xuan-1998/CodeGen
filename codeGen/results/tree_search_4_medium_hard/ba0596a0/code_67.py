from sys import stdin

def can_frog_cross(stones):
    dp = [[False for _ in range(3)] for _ in range(len(stones))]

    dp[0][1] = True  # base case: frog starts on first stone
    for i in range(1, len(stones)):
        for k in [1, 2]:
            if dp[i - 1][k + 1]:  # check if frog can reach current stone from previous one
                dp[i][k] = True  # update dp table with solution to smaller subproblem

    return any(dp[-1])  # check if frog can reach last stone and return result

# Read input from stdin
stones = [int(x) for x in stdin.readline().split()]

print(can_frog_cross(stones))
