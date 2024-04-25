def min_sum_binary_matrix(N, M):
    return min(N, M)

def main():
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        result = min_sum_binary_matrix(N, M)
        print(result)

if __name__ == "__main__":
    main()
