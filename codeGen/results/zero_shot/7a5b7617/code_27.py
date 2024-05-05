import sys

def steady_tables(N, M):
    return pow(M + 1, N) * (M + 1) % 1000000000

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(steady_tables(N, M))
