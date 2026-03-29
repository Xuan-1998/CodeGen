import sys

def solve():
    T = int(input())
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))
        
        # Sort the hemispheres by radius
        U.sort()
        L.sort()
        
        # Initialize a dictionary to store the count of each sequence length
        seq_count = {i: 0 for i in range(C+1)}
        
        # Count the number of sequences for each length
        for u in U:
            for l in L:
                if u >= l:
                    for i in range(min(u, l)+1):
                        seq_count[i] += 1
        
        # Calculate the answer
        ans = 0
        for i in range(C+1):
            ans += seq_count[i]
        
        print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
