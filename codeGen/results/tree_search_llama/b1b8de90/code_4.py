def recursive_sort(arr, n):
    if len(arr) <= 1:
        return arr

    pivot = arr[n-1]
    left = [x for x in arr[:n-2] if x < pivot]
    middle = [x for x in arr[:n-2] if x == pivot]
    right = [x for x in arr[:n-2] if x > pivot]

    return recursive_sort(left + middle + right + [pivot], n-1)

def main():
    n = int(input())
    permutation = list(range(1, n+1))
    random.shuffle(permutation)
    
    sorted_permutation = recursive_sort(permutation, len(permutation))
    print(' '.join(map(str, sorted_permutation)))

if __name__ == "__main__":
    main()
