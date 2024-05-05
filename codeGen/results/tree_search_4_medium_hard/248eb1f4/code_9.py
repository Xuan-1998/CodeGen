import sys

def solve_memoization():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        m, x = map(int, sys.stdin.readline().strip().split())
        dp = {0: 1}
        last_winner = 1
        for i in range(1, x+1):
            if i % (m-1) == 0:
                last_winner = (last_winner - m + 2) % (x+1)
            else:
                last_winner = (last_winner - 1) % (x+1)
            dp[i] = last_winner
        print(*dp.values(), sep='\n')

solve_memoization()
