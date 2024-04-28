def count_ways(m, N):
    # Initialize dp_dict
    dp_dict = {(0, j): 1 for j in range(m+1)}
    
    for i in range(1, N+1):
        for j in range(min(i+1, m)+1):
            if i > 0:
                if j > 0:
                    dp_dict[(i, j)] = sum(dp_dict.get((i-k, k-1), 0) for k in range(1, min(i+1, j)+1))
                else:
                    dp_dict[(i, j)] = 1
            else:
                if j > 0:
                    dp_dict[(i, j)] = 0
                else:
                    dp_dict[(i, j)] = 1
    
    return dp_dict.get((N, m), 0) % (10**9 + 7)

# Read inputs from stdin
m, N = map(int, input().split())
arr = list(map(int, input().split()))

print(count_ways(m, N))
