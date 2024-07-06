python
def modular_exponentiation(base, exponent, mod):
    result = 1
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2
    return result

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    MOD = 998244353
    result = modular_exponentiation(M + 1, N, MOD)
    
    print(result)

if __name__ == "__main__":
    solve()

