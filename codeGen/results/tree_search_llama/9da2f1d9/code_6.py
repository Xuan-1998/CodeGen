def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    
    for j in range(low, high+1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def three_way_partition(arr, low, high):
    if low < high:
        pivot1 = partition(arr, low, high)
        i = 0
        j = pivot1-1
        k = pivot1 + 1
        
        while True:
            if arr[j] <= arr[low]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif arr[k] > arr[low]:
                arr[i+1], arr[k] = arr[k], arr[i+1]
                i += 1
                k += 1
            else:
                break
                
        return (i+1), pivot1, k

def main():
    size = int(input())
    arr = list(map(int, input().split()))
    pivot = int(input())

    low = 0
    high = size-1
    
    left, right = three_way_partition(arr, low, high)
    
    for i in range(left):
        print(arr[i], end=' ')
    for i in range(right-size+1):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
