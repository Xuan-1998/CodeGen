def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    MOD = 998244353
    
    result = (pow(2, N, MOD) * pow(2, M, MOD)) % MOD
    print(result)


