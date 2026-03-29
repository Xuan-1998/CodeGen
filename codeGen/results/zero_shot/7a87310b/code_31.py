import sys

def count_matrices():
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        
        count = 0
        
        for i in range(1, N//2 + 1):
            if N - 2*i >= 0:
                count += (N - 2*i) // i
                
        print(count)

count_matrices()
