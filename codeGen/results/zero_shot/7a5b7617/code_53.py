import sys

def solve(n, m):
    MOD = 10**9 + 7
    total_sum = n * (n - 1) // 2 * m
    result = 0
    for i in range(total_sum, -1, -m):
        if i <= M:
            result += 1
    return result % MOD

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(solve(n, m))
