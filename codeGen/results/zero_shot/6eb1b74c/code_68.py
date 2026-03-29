import sys
from math import ceil

def solve():
    t = input().strip()
    n = int(input())
    freqs = {}
    
    # Calculate frequency of each string
    for _ in range(n):
        s = input().strip()
        freqs[s] = t.count(s)
    
    # Calculate the minimum number of steps
    m = sum(ceil(freq / len(s)) - 1 for s, freq in freqs.items()) if freqs else -1
    
    if m == -1:
        print(-1)
    else:
        print(m)
        
        # Print the pairs of indices: w_j and p_j
        for i, (s, freq) in enumerate(freqs.items(), 1):
            p = 0
            while True:
                pos = t.find(s, p)
                if pos == -1:
                    break
                print(f"{i} {pos}")
                p = pos + len(s)

if __name__ == "__main__":
    solve()
