MOD = 998244353

def count_valid_matrices(N, M):
    total_count = 0
    
    for top in range(N):
        for left in range(M):
            for bottom in range(top, N):
                for right in range(left, M):
                    # Number of 1's in the rectangle
                    num_ones = (bottom - top + 1) * (right - left + 1)
                    # Total elements in the matrix
                    total_elements = N * M
                    # Number of 0's outside the rectangle
                    num_zeros = total_elements - num_ones
                    # Each 0 can be either 0 or 1 independently
                    total_count += pow(2, num_zeros, MOD)
                    total_count %= MOD
    
    return total_count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    result = count_valid_matrices(N, M)
    print(result)

