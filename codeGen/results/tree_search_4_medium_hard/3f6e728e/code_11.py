from sys import stdin, stdout

def solve():
    T = int(stdin.readline())
    for _ in range(T):
        N, M, C = map(int, stdin.readline().split())
        U = list(map(int, stdin.readline().split()))
        L = list(map(int, stdin.readline().split()))
        F = [0] * (C + 1)
        F[0] = 1
        for i in range(C):
            for j in range(N):
                if U[j] > i:
                    F[i] += F[i - U[j]]
            for k in range(M):
                if L[k] > i:
                    F[i] -= F[i - L[k]]
        stdout.write(' '.join(map(str, [F[i] % (10**9 + 7) for i in range(C)])) + '\n')

if __name__ == "__main__":
    solve()
