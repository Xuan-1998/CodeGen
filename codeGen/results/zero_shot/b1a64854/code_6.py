def min_sum_for_binary_matrix(N, M):
    # The minimum sum is achieved by creating a square submatrix of 1s
    # with size equal to the smaller of N and M.
    return min(N, M) ** 2

def main():
    T = int(input().strip())  # Number of test cases
    for _ in range(T):
        N, M = map(int, input().split())  # Read the dimensions of the matrix
        print(min_sum_for_binary_matrix(N, M))  # Calculate and print the minimum sum

if __name__ == "__main__":
    main()
