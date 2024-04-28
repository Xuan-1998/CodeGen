from collections import defaultdict

def count_paths(K, N, arr):
    dp_dict = defaultdict(int)
    dp_dict[0][0] = 1 if arr[0][0] == K else 0
    
    for i in range(1, N):
        for j in range(N):
            dp_dict[i][j] = (dp_dict.get((i-1)[j], 0) + 
                              dp_dict.get((i)[j-1], 0))
    
    return dp_dict[N-1][N-1]
