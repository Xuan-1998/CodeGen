python
import sys

def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    remaining = arr[0]
    for i in range(1, n):
        remaining -= arr[i]
    
    return remaining

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    result = max_remaining_element(n, arr)
    print(result)

