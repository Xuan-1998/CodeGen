import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        # Sort the radii of upper and lower hemispheres
        U.sort()
        L.sort()

        # Initialize the count of X-sequences for each length
        Cnt = [0] * (C + 1)

        # Iterate over the radii of upper hemispheres
        for i in range(N):
            j = U[i]
            # Iterate over the radii of lower hemispheres
            for k in range(M):
                l = L[k]
                # Update the count of X-sequences for each length
                Cnt[min(j, l) + 1] += (C - min(j, l)) * ((j == l and i < M) or (i >= M and j < l))

        # Print the count of X-sequences for each length modulo 10^9+7
        print(*[(x - y) % (10**9 + 7) for x, y in zip(Cnt[1:], Cnt)], sep=' ')

if __name__ == "__main__":
    solve()
