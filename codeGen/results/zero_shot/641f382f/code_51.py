function main():
    # Read input
    n = int(input())
    array = list(map(int, input().split()))

    # Check if 1 is already in the array
    if 1 in array:
        print(0)
        return

    # Initialize the minimum operations to a large number
    min_operations = float('inf')

    # Check for each element if we can make the array equal to 1
    for i in range(n):
        current_gcd = array[i]
        for j in range(i+1, n):
            current_gcd = gcd(current_gcd, array[j])
            # If we find a GCD of 1, update the minimum operations
            if current_gcd == 1:
                min_operations = min(min_operations, j - i)
                break

    # If we never found a GCD of 1, it is impossible to make the array equal to 1
    if min_operations == float('inf'):
        print(-1)
    else:
        # The total operations is the sum of operations to get a single 1 and to make the rest of the array 1
        print(min_operations + n - 1)

# Euclid's algorithm for finding the GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

main()
