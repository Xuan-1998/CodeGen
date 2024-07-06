python
def main():
    import sys
    input = sys.stdin.read
    MOD = 998244353
    
    N, M = map(int, input().strip().split())
    
    # Compute the number of valid matrices.
    # The number of valid matrices is 2^(N+M-1)
    result = pow(2, N + M - 1, MOD)
    
    print(result)

if __name__ == "__main__":
    main()

