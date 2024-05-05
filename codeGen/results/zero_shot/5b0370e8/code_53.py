python
# Let's start by initializing a variable to store the total count.
total_count = 0

for _ in range(int(input())):
    n, k = map(int, input().split())
    # For each test case, we need to calculate the bitwise AND and XOR of all elements.
    # To make it easier to calculate, let's first calculate the maximum possible value for each operation.

    max_and = (1 << k) - 1
    max_xor = (1 << k) - 1

    count = 0
    for _ in range(n):
        x = int(input())
        # For each element, we need to check if the bitwise AND is greater than or equal to the bitwise XOR.
        if (x & max_and) >= (x ^ max_xor):
            count += 1

    total_count += count
    print(count % (10**9 + 7))
