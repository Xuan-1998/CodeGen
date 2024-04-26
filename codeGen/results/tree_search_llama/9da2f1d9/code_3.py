def partition(arr, low, high, pivot):
    # Partition the array around the pivot element
    i = low - 1
    for j in range(low, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i + 1

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    pivot = int(input())

    # Implement the partitioning step here
    pivot_index = partition(arr, 0, n - 1, pivot)

    print(" ".join(str(x) for x in arr[:pivot_index]))  # Print elements less than the pivot
    print(" ".join(str(x) for x in arr[pivot_index:]))
