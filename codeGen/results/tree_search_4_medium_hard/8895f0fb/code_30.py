import sys
from collections import defaultdict

def expected_non_zero_carry(n):
    dp = defaultdict(int)
    dp[(0, 0)] = 0.5
    for i in range(1, n+1):
        for j in range(i+1):
            if (j % 10) + ((i-j-1)//10) >= 10:
                c = (j % 10) - (9-(i-j-1)%10)
            else:
                c = 0
            if i == n:
                dp[(i, j)] = c * 0.5
            else:
                dp[(i, j)] += dp[(i-1, c)]
    return sum([dp[(n, int('1'*n)-k)] for k in range(int('1'*n))]) / (int('9'*(n-1))+1)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(expected_non_zero_carry(n))
