def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print((M + 1) % 1000000000)
