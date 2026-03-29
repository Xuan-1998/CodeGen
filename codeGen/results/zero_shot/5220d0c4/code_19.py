def beauty(n):
    pass

def calculate_beauty(arr):
    return [beauty(x) for x in arr]

def max_beauty(arr):
    return max(calculate_beauty(arr))

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Calculate and print the maximum beauty of the array
print(max_beauty(arr))
