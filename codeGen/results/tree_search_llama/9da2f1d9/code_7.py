import sys

def partition(arr, pivot):
    # Initialize three lists: left, middle, and right
    left = []
    middle = []
    right = []

    # Partition the array into three parts based on the pivot element
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return left + middle + right

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    pivot = int(sys.stdin.readline())

    result = partition(arr, pivot)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
