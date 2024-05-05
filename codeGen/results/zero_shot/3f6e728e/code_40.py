import sys

def solve():
    T = int(input())
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        # Initialize the result array with zeros
        res = [0] * (C + 1)
        
        for r in set(U):
            if r <= C:
                res[r] += len([x for x in U if x == r])
                
        for r in set(L):
            if r <= C:
                res[r] += len([x for x in L if x == r])
        
        # Calculate the result modulo 10^9+7
        mod = 10**9 + 7
        for i in range(C + 1):
            res[i] %= mod
        
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    solve()
