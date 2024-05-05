import heapq
from collections import defaultdict, deque
mod = 10**9 + 7

def solve():
    n = int(input())
    edges = list(map(lambda x: list(map(int, x.split())), [input().split() for _ in range(n-1)]))
    
    # Step 1: Build a tree using the given edges
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Step 2: Compute the prime factors of k
    m = int(input())
    primes = list(map(int, input().split()))
    
    # Step 3: Find the maximum possible distribution index
    max_index = 0
    for _ in range(m):
        # Step 3.1: Find a prime p that does not appear as a factor in k
        p = next((p for p in primes if all(p % q for q in primes)), None)
        
        # Step 3.2: Label the edges with numbers and update the maximum possible distribution index
        for u, v in edges:
            fuv = 1
            while tree[u]:
                w = tree[u].pop()
                if w != v:
                    tree[u].append(w)
                    w = None
                    break
                fuv *= p
                u = w
            max_index += fuv
    
    print(max_index % mod)

if __name__ == "__main__":
    solve()
