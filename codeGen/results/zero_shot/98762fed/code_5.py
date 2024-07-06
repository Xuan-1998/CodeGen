def count_ones(N, M):
    MOD = 998244353
    
    # Number of ones in a rectangle of size a x b is a * b
    # We need to sum over all possible rectangles
    total_ones = 0
    for a in range(1, N + 1):
        for b in range(1, M + 1):
            total_ones += a * b
            total_ones %= MOD
    
    return total_ones

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    print(count_ones(N, M))

