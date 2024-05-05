def count_sequences(N, M, C):
    upper_rads = set(U_rads)
    lower_rads = set(L_rads)
    sequences = [0] * (C + 1)

    for rad in range(1, C + 1):
        sequences[rad] += len([x for x in upper_rads if x <= rad])
        sequences[rad] += len([x for x in lower_rads if x >= rad])

    return [seq % (10**9 + 7) for seq in sequences[1:]]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U_rads = list(map(int, input().split()))
        L_rads = list(map(int, input().split()))
        print(*count_sequences(N, M, C), sep=" ")
