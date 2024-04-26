import sys

def partition(arr, pivot):
    # Initialize pointers for left and right partitions
    left = 0
    right = len(arr) - 1
    
    while True:
        # Move the left pointer to the right until we find an element that is greater than or equal to the pivot
        while arr[left] < pivot and left < right:
            left += 1
        
        # Move the right pointer to the left until we find an element that is less than or equal to the pivot
        while arr[right] >= pivot and left <= right:
            right -= 1
        
        if left >= right:
            break
        
        # Swap elements at the left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
    
    return left, right

def main():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    pivot = int(sys.stdin.readline().strip())

    # Partition the array
    left, right = partition(arr, pivot)

    # Print the result
    for i in range(len(arr)):
        if i < left:
            print(str(arr[i]), end=' ')
        elif i == left:
            print(str(pivot), end=' ')
        else:
            print(str(arr[i]), end=' ')

if __name__ == "__main__":
    main()
