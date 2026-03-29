import sys

t = int(input())  # Read the number of test cases
for _ in range(t):
    n, m = map(int, input().split())  # Read the initial number and number of operations
    length = len(str(n))  # Initial length of the number
    for _ in range(m):
        new_n = int(''.join(map(lambda x: str((int(x) + 1) % 10), str(n))))  # Apply one operation
        length += (len(str(new_n)) - len(str(n)))  # Update the length
        n = new_n  # Update the number
    print(length % (10**9+7))  # Print the final length modulo 10^9+7
