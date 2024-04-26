def merge_arrays(*args):
    max_length = max(len(arr) for arr in args)
    result = []
    
    for i in range(max_length):
        for arg in args:
            if i < len(arg):
                result.append(arg[i])
            else:
                result.append(None)
    
    return result

if __name__ == "__main__":
    arrays = [list(map(int, input().split())) for _ in range(int(input()))]
    print(merge_arrays(*arrays))
