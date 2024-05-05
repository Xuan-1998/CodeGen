import sys
from math import gcd
from functools import reduce

def main():
    T = int(input())
    MOD = 10**9 + 7
    
    for _ in range(T):
        n, *edges = map(int, input().split())
        m, *prime_factors = map(int, input().split())
        
        state = [[0] * (n-1) for _ in range(n)]
        state[0][0] = 0
        
        children = [0] * n
        for u, v in zip(*[iter(edges)]*2):
            children[u-1] += 1
            children[v-1] += 1
            
        for i in range(1, n):
            state[i][0] = state[i-1][children[i-1]-1]
            
        for i in range(n-2, -1, -1):
            for j in range(1, min(i+1, children[i])):
                if gcd(j, prime_factors[0]) != 1:
                    continue
                prime_factors = [p for p in prime_factors[1:]]
                
                if not prime_factors or len(prime_factors) == m-1:
                    state[i][j] = state[i][j-1]
                else:
                    state[i][j] = reduce(gcd, [gcd(j, p) for p in prime_factors])
                    
        print(sum((state[i][1:] or [0]) for i in range(n)) % MOD)

if __name__ == "__main__":
    main()
