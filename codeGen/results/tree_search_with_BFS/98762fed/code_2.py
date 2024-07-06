python
def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    MOD = 998244353
    
    # Calculate 2^M % MOD
    power_of_two = pow(2, M, MOD)
    
    # Calculate (2^M)^N % MOD
    result = pow(power_of_two, N, MOD)
    
    print(result)

if __name__ == "__main__":
    solve()

