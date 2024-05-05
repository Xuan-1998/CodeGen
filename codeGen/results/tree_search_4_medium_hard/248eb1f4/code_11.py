import sys

input()
T = int(sys.stdin.readline())
for _ in range(T):
    M, X = map(int, sys.stdin.readline().split())
    dp = {0: 1}
    for i in range(1, X+1):
        dp[i] = (i-1) % M + dp.get((i-1)//M, i-1)
        last_winner = (dp.get((i-1)//M, i-1) - ((i-1)//M)//M*M) % i
        dp[i] = last_winner
    print(' '.join(map(str, [x+1 for x in dp.values()])))
