def min_sum_for_matrix(N, M):
    if N != M:
        return 0
    else:
        return N

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = min_sum_for_matrix(N, M)
        print(result)

if __name__ == "__main__":
    main()
