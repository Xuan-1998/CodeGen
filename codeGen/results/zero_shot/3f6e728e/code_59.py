T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    U = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for _ in range(T):
        N, M, C = N, M, C
        U.sort()
        L.sort()
        for i in range(1, C+1):
            ways_to_build_i_sequence = 1
            j = 0
            k = len(L) - 1
            while j <= len(U) - 1 and k >= 0:
                if U[j] < i:
                    j += 1
                elif L[k] > i:
                    k -= 1
                else:
                    ways_to_build_i_sequence = (ways_to_build_i_sequence * (j + 1)) % (10**9 + 7)
                    while j <= len(U) - 1 and U[j] < i:
                        j += 1
                    while k >= 0 and L[k] > i:
                        k -= 1
            print(ways_to_build_i_sequence, end=' ')
        print()
