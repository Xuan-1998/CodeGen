from sys import stdin

def solve():
    n = int(stdin.readline())
    moods = list(map(int, stdin.readline().split()))

    # Initialize the memoization table
    memo = [[False] * (n + 1) for _ in range(n + 1)]

    # Base cases
    memo[0][0] = True

    for i in range(1, n + 1):
        memo[i][i] = moods[i - 1] == 1
        for j in range(i):
            if moods[j] == 1:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = False

    # Print the result
    print("YES" if memo[n][n] else "NO")

solve()
