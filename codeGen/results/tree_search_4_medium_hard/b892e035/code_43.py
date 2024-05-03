import sys

def correct_numbering_probability(n):
    memo = {}
    dp = [[[0.0 for _ in range(17)] for _ in range(17)] for _ in range(n+1)]

    for i in range(1, n+1):
        for a in range(1, 17):
            for b in range(1, 17):
                if (a, b) not in memo:
                    memo[(a, b)] = (p/100.0) * ((1-p)/100.0)
                dp[i][a][b] = (dp[i-1][a][b]*(p/100.0) * ((1-p)/100.0)) + (dp[i-1][a][b]*(q/100.0) * ((1-q)/100.0))

    return sum([dp[n][i][j] for i in range(1, 17) for j in range(1, 17)])

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        p = [int(input()) for _ in range(n)]
        q = [int(input()) for _ in range(n)]
        print('%.6f' % correct_numbering_probability(n))

if __name__ == '__main__':
    main()
