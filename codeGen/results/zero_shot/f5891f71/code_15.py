import sys
input = sys.stdin.read

def max_remaining_element(n, arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Perform the operations
    while len(arr) > 1:
        # Always subtract the last element from the first element
        arr[0] -= arr.pop()
    
    # The remaining element is the result
    return arr[0]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    print(max_remaining_element(n, arr))

