import sys
from itertools import cycle

def merge_arrays(*args):
    max_len = max(len(arg) for arg in args)
    result = []
    
    for i in range(max_len):
        for arg in args:
            if i < len(arg):
                result.append(arg[i])
            else:
                result.append(None)
                
    return result

if __name__ == "__main__":
    input_arrays = []
    
    while True:
        try:
            array = list(map(int, input().split()))
            input_arrays.append(array)
        except EOFError:
            break
    
    print(merge_arrays(*input_arrays))
