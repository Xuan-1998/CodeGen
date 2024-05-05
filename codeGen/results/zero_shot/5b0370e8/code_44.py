python
def count_arrays(n, k):
    # Count the number of arrays for which the result of the bitwise AND operation on all elements is greater than or equal to the result of the bitwise XOR operation on all elements.

    # Calculate the maximum possible bitwise AND value and bitwise XOR value.
    max_and = (1 << k) - 1
    max_xor = (1 << k) - 1

    # Initialize the count to 0.
    count = 0

    # Iterate over each array of length n, considering all possible values for each element in the range [0, 2^k-1].
    for mask in range((1 << k) - 1):
        and_val = 0
        xor_val = 0
        # Calculate the bitwise AND and XOR values for this array.
        for i in range(n):
            val = (mask >> i) & ((1 << k) - 1)
            and_val |= val
            xor_val ^= val

        # Check if the bitwise AND value is greater than or equal to the bitwise XOR value, and increment the count if it is.
        if and_val >= xor_val:
            count = (count + 1) % (10**9 + 7)

    return count

# Read the test cases from standard input.
t = int(input())

# Process each test case.
for _ in range(t):
    n, k = map(int, input().split())
    print(count_arrays(n, k))
