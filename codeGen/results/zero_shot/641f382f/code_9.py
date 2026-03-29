function gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

function min_operations(arr):
    # Check if the GCD of the entire array is 1
    array_gcd = arr[0]
    for i in range(1, len(arr)):
        array_gcd = gcd(array_gcd, arr[i])
    if array_gcd > 1:
        return -1

    operations = 0
    for i in range(len(arr)):
        # If the element is already 1, continue
        if arr[i] == 1:
            continue
        current_gcd = arr[i]
        # Find the minimum operations for each element
        for j in range(i + 1, len(arr)):
            current_gcd = gcd(current_gcd, arr[j])
            if current_gcd == 1:
                operations += j - i
                break
    return operations

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(min_operations(arr))
