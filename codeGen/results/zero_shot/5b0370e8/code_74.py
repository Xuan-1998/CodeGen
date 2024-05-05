import sys

def solve():
    t = int(input())
    mod = 10**9 + 7
    
    for _ in range(t):
        n, k = map(int, input().split())
        and_result = xor_result = 0
        
        for _ in range(n):
            a = int(input())
            and_result |= a
            xor_result ^= a
        
        count = 1 if and_result >= xor_result else 0
        print(count % mod)

solve()
