import sys

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, X = map(int, sys.stdin.readline().split())
        A = list(map(int, sys.stdin.readline().split()))
        
        # Compute the XOR sum without adding X to any subsequence
        xor_sum = 0
        for i in range(1, N):
            xor_sum ^= A[i-1] ^ A[i]
        
        # Try adding X to each subsequence and find the maximum XOR value
        max_xor = 0
        for i in range(N):
            new_xor_sum = xor_sum
            for j in range(i+1, N):
                new_xor_sum ^= (A[j-1] ^ A[j]) + X if j > i else A[j-1] ^ A[j]
                max_xor = max(max_xor, new_xor_sum)
        
        print(max_xor)

if __name__ == '__main__':
    solve()
