import sys

def main():
    q = int(sys.stdin.readline().strip())
    
    for _ in range(q):
        u, v = map(int, sys.stdin.readline().strip().split())
        
        # Initialize dp array with base cases
        dp = [1] * (2**30)
        
        # Iterate over each bit in v from most significant to least significant
        for i in range(30, -1, -1):
            # If the ith bit is 0, it means there's no edge from any vertex to a new vertex with that bit set to 1
            if not (v & (1 << i)):
                dp = [x >> 1 for x in dp]
            else:
                # If the ith bit is 1, it means there's an edge from all reachable vertices to a new vertex
                dp = [(x | (2**i)) for x in dp]
        
        # The final state, dp[v], will represent the number of vertices reachable by v
        if dp[v] > 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
