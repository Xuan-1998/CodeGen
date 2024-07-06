python
def main():
    import sys
    input = sys.stdin.read
    MOD = 998244353

    # Read input
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])

    # Calculate the number of valid matrices
    total_matrices = pow(2, N * M, MOD)

    # Output the result
    print(total_matrices)

if __name__ == "__main__":
    main()

