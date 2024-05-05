import sys

def has_path(u, v):
    # Base case: If u is equal to v, then we have found a path
    if u == v:
        return "YES"
    
    # Pruning: Since u & v = v, all intermediate vertices must also satisfy u & v = v
    # So, we can prune the search space by only considering vertices that satisfy this condition
    for i in range(u + 1, v):
        if (i & v) != v:
            return "NO"  # No path found
    
    return has_path(u, (u & v))  # Recursively search for a path from u to v

def main():
    q = int(sys.stdin.readline())
    
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        
        print(has_path(u, v))

if __name__ == "__main__":
    main()
