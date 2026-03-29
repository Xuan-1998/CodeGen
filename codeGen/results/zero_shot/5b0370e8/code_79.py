import sys

def solve():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        ans = 0
        for _ in range(n):
            x = int(input())
            
            and_result = (x & ((1 << k) - 1))
            xor_result = x ^ ((1 << k) - 1)
            
            if and_result >= xor_result:
                ans += 1
        
        print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
