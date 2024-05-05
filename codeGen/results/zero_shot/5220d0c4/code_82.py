def max_beauty(arr, bad_primes):
    # Define the maximum beauty variable
    max_beauty = 0

    # Iterate over all possible subsets of the array
    for i in range(1 << len(arr)):
        subset = [arr[j] for j in range(len(arr)) if (i & (1 << j))]
        total_beauty = beauty(subset, bad_primes)
        max_beauty = max(max_beauty, total_beauty)

    return max_beauty


# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Calculate and print the maximum beauty
print(max_beauty(arr, bad_primes))
