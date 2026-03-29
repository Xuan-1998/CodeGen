# Read input
T = int(input())
for _ in range(T):
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    m = int(input())
    prime_factors = list(map(int, input().split()))
    
    # Sort the edges
    edges.sort()
    
    # Initialize the current product and the result
    curr_product = 1
    res = 0
    
    # Iterate over all pairs of nodes
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the sum of the numbers on the simple path from node i to node j
            f = 1
            curr_u = i
            while curr_u != j:
                for edge in edges:
                    if edge[0] == curr_u and edge[1] == k:
                        curr_u = edge[1]
                        f *= curr_product
                        break
                    elif edge[0] == curr_u and edge[1] == k:
                        curr_u = edge[0]
                        f *= curr_product
                        break
            # Update the result
            res += f
    print(res % (10**9 + 7))
