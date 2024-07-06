def solve():
    import sys
    input = sys.stdin.read
    MOD = 998244353

    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])

    # For any matrix configuration, the valid matrices are those that can be
    # constructed by ensuring the condition holds for all (a, b, c, d).
    # This can be achieved by ensuring that the matrix is either all 0s or all 1s.
    # Hence there are 2^MN valid matrices.
    
    # Calculate 2^(N*M) % MOD
    result = pow(2, N * M, MOD)
    
    # Print the result
    print(result)


