def solve():
    global C, mod
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        dp = [0] * (C+1)
        mod = 10**9 + 7
        print(*[count_sequences(U[:i], N) * count_sequences(L[:j], M) for i in range(N+1) for j in range(M+1)], sep=' ')
