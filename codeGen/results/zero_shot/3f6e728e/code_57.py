import sys

def solve(N, M, C):
    MOD = 10**9 + 7
    f = [0] * (C + 1)
    f[0] = 1
    for i in range(1, C + 1):
        if N > 0:
            f[i] += f[i-1] * (N - U_1) % MOD
            N -= U_1
        if M > 0:
            f[i] += f[i-2] * (M - L_1) % MOD
            M -= L_1
    return ' '.join(map(str, [f[i] for i in range(C + 1)]))

T = int(sys.stdin.readline())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    U_1 = list(map(int, sys.stdin.readline().split()))
    L_1 = list(map(int, sys.stdin.readline().split()))
    print(solve(N, M, C))
