import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        
        # Find the maximum value without adding X to any subsequence
        max_value = 0
        for i in range(2, N+1):
            max_value += A[i-1] ^ A[i]
        
        # Try to add X to at most one subsequence to increase the value
        max_value += X
        
        print(max_value)

if __name__ == '__main__':
    solve()
