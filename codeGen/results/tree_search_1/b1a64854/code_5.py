def min_sum_binary_matrix(N, M):
    # The minimum sum will be the smaller of the two dimensions
    return min(N, M)

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = min_sum_binary_matrix(N, M)
        print(result)

if __name__ == "__main__":
    main()
