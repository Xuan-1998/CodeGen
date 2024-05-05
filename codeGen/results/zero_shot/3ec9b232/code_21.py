import sys

def solve():
    n = int(sys.stdin.readline())
    m = list(map(int, sys.stdin.readline().split()))
    
    T = 1
    for i in range(n):
        # Calculate the number of ways to create arrays that will sort to m_i when merged with all previous elements
        ways_to_create_arrays = 1
        for j in range(i+1):
            ways_to_create_arrays *= (m[i] - j)
        
        # Multiply this number by the total number of ways to create arrays for the remaining elements
        T *= ways_to_create_arrays
        
    print(T % (10**9 + 7))

if __name__ == "__main__":
    solve()
