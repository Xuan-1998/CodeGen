python
def count_valid_matrices(N, M):
    MOD = 998244353
    
    # Calculate the number of valid matrices
    # Each row can be independently filled with 0s and 1s such that once a 1 appears, all subsequent elements in that row must be 1.
    # There are M + 1 ways to fill each row (0 ones, 1 one, ..., M ones).
    # So, the number of ways to fill one row is (M + 1).
    # Since rows are independent, the total number of matrices is (M + 1)^N.
    
    result = pow(M + 1, N, MOD)
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_valid_matrices(N, M))

