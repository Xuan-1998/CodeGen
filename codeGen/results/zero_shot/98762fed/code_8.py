python
def count_valid_matrices(N, M):
    MOD = 998244353

    # We need to count the number of valid matrices
    # Each row and each column can be seen as a binary string of length M and N respectively
    # The number of valid binary strings of length k is 2^k because each position can be either 0 or 1 independently

    # Total number of valid matrices is (2^M)^N because each row can be chosen independently
    result = pow(2, N * M, MOD)
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    print(count_valid_matrices(N, M))

