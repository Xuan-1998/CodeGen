import sys

def solve(n, k):
    # Calculate the number of bits set to 1 in the binary representation of each element
    bit_counts = [bin(i)[2:].count('1') for i in range(2**k)]
    
    # Initialize the count of arrays that satisfy the condition
    count = 0
    
    # Iterate over all possible combinations of bits
    for bits in zip(*[iter(bit_counts)]*n):
        # Calculate the bitwise AND and XOR operations on the current combination of bits
        and_op = sum(1 << i for i, bit in enumerate(bits) if bit)
        xor_op = sum(1 << i for i, bit in enumerate(bits) if not bit)
        
        # Check if the bitwise AND operation is greater than or equal to the bitwise XOR operation
        if and_op >= xor_op:
            count += 1
    
    # Return the count modulo $10^9+7$
    return count % (10**9 + 7)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
