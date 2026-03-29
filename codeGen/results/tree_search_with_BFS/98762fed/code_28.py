def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    MOD = 998244353
    
    # The number of ones in the largest possible monotonic submatrix of size N x M
    result = (N * M) % MOD
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()

