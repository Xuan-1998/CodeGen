import sys

def calculate_stable_tables(N, M):
    # Initialize the count of stable tables
    count = 0
    
    # Iterate over all non-negative integers from 0 to M - 1 for each element in the table
    for row in range(N):
        for col in range(M):
            # For each element, calculate the sum of elements in the ith row
            total = 0
            for j in range(col + 1):
                total += 1
            
            # If the sum of elements in the ith row is not less than the sum of elements in the (i-1)th row and 
            # the sum of elements in the Nth row is less than or equal to M, increment the count
            if total <= min(N - row - 1, M):
                count = (count + 1) % 1000000000
    
    return count

# Read input from standard input
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    # Calculate and print the number of different steady tables of size N x M modulo 1 000 000 000
    print(calculate_stable_tables(N, M))
