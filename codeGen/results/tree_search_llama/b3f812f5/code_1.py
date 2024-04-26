def find_indices():
    N = int(input())
    Arr = list(map(int, input().split()))
    
    result = []
    index_dict = {}
    
    for i in range(N):
        if Arr[i] == i + 1:  # 1-based indexing
            index_dict[i + 1] = i
    
    for key in index_dict:
        result.append(index_dict[key])
    
    print(result)

find_indices()
