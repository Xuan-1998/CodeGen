def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    MOD = 998244353
    
    # Calculate (M+1)^N % 998244353
    result = pow(M + 1, N, MOD)
    
    print(result)


