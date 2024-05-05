===BEGIN CODE===
import sys
from collections import namedtuple

Input = namedtuple('Input', 'n a b c')

def solve(input):
    n = input.n
    a = list(map(int, input.a.split()))
    b = list(map(int, input.b.split()))
    c = list(map(int, input.c.split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == 1:
            dp[i][0] = max(c[0], b[0])
            dp[i][1] = c[0]
        else:
            for j in range(min(i, n) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][max(0, j - 1)]) + (a[i - 1] if j == 0 else b[i - 1])

    return dp[n][n]

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    input_ = Input(n, ' '.join(map(str, a)), ' '.join(map(str, b)), ' '.join(map(str, c)))
    print(solve(input_))

if __name__ == '__main__':
    main()
===END CODE===
