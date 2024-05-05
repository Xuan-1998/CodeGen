def calculate_beauty(arr):
    # TO DO: implement this function
    pass

def find_max_beauty(n, m, arr, bad_primes):
    max_beauty = 0
    for i in range(1 << n):  # iterate over all subsets of the array
        subset_sum = sum([arr[j] for j in range(n) if (i & (1 << j))])
        beauty = calculate_beauty(subset_sum)
        if beauty > max_beauty:
            max_beauty = beauty
    return max_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(find_max_beauty(n, m, arr, bad_primes))
