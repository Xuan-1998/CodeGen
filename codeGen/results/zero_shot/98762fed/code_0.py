python
MOD = 998244353

def count_valid_matrices(N, M):
    # For any row, there are 2^M possible configurations (since each element can be 0 or 1)
    # For each configuration, it must be consistent across all rows.
    # Therefore, we need to count the number of valid configurations.
    
    # The number of valid matrices is 2^M (each row can be any of the 2^M configurations)
    result = pow(2, M, MOD)
    
    # Since there are N rows, each configuration can be repeated across N rows
    # Therefore, the total number of valid matrices is (2^M)^N
    result = pow(result, N, MOD)
    
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    print(count_valid_matrices(N, M))

