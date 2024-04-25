def min_sum_binary_matrix(N, M):
    # The minimum sum is the square of the smaller dimension
    return min(N, M) ** 2

def main():
    T = int(input().strip())  # Read the number of test cases
    for _ in range(T):
        N, M = map(int, input().split())
        result = min_sum_binary_matrix(N, M)
        print(result)

if __name__ == "__main__":
    main()
