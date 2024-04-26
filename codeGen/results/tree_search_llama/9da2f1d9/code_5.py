def partition(arr, low, high, pivot):
    i = low - 1
    j = low

    while j <= high:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[j] == pivot:
            j += 1
        else:
            high -= 1
            arr[high + 1], arr[j] = arr[j], arr[high + 1]

    return i, high

def partition_around_pivot(arr, low, high, pivot):
    if low >= high:
        return []

    left, right = partition(arr, low, high, pivot)
    return [arr[i] for i in range(low, left)] + \
           [arr[i] for i in range(left + 1, right + 1)] + \
           [arr[i] for i in range(right + 2, high + 1)]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    pivot = int(input())

    result = partition_around_pivot(arr, 0, n - 1, pivot)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
