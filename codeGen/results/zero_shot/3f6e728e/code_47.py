def solve():
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))

    unique_radii = set(U) | set(L)
    num_sequences = len(unique_radii)

    print(*[num_sequences % (10**9 + 7)] * C, sep=' ')

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
