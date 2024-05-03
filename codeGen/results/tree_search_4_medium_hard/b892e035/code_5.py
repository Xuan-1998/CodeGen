import sys

def probability_of_correct_numbering():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        dp = [[[0.0 for _ in range(17)] for _ in range(17)] for _ in range(51)]
        
        for i in range(n):
            p1, a1, b1 = map(int, sys.stdin.readline().split())
            p2, a2, b2 = map(int, sys.stdin.readline().split())
            
            dp[i+1][a1][b1] += (p1 * (1 - sum(dp[j][k][l] for j in range(i) for k in range(17) for l in range(17)))) * (p1 / 100.0)
            dp[i+1][a2][b2] += (p2 * (1 - sum(dp[j][k][l] for j in range(i) for k in range(17) for l in range(17)))) * (p2 / 100.0)
        
        print(sum([dp[n][i][j] for i in range(17) for j in range(17)]))

probability_of_correct_numbering()
