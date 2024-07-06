python
import sys
import math

MOD = 998244353

def comb(n, k):
    if k > n:
        return 0
    return math.comb(n, k) % MOD

def solve():
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    # Calculate the number of valid matrices
    result = comb(N + M - 2, N - 1)
    
    print(result)

if __name__ == "__main__":
    solve()

