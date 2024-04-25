def min_sum_for_matrix(N, M):
    # If N equals M, the minimum sum is N (or M, since N = M).
    # Else, it is not possible to satisfy the condition, so the sum is 0.
    return N if N == M else 0

def main():
    T = int(input().strip())  # Read number of test cases
    for _ in range(T):
        N, M = map(int, input().strip().split())  # Read N and M for each test case
        print(min_sum_for_matrix(N, M))  # Calculate and print the minimum sum

if __name__ == "__main__":
    main()
