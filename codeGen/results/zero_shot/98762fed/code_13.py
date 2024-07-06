MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    N, M = map(int, input().split())
    
    # The number of valid matrices is 2^(N + M - 1)
    # Explanation: We can independently choose the value for each row and column.
    # The first element of each row and each column can be either 0 or 1.
    # This gives us 2^(N + M - 1) valid configurations.
    
    result = pow(2, N + M - 1, MOD)
    print(result)

if __name__ == "__main__":
    solve()

