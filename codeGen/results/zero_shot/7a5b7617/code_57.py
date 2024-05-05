import sys
from math import factorial

def steady_tables(n, m):
    # Calculate the number of ways to fill the first row
    first_row_ways = 1
    for i in range(1, n+1):
        first_row_ways *= (m + 1 - i)
    
    # For each subsequent row, calculate the number of ways to fill it given the sum is at least as large as the previous row's sum
    total_ways = factorial(m + n) // (factorial(n) * factorial(m))
    for i in range(2, n+1):
        total_ways *= (i-1)
    
    return total_ways % 1000000000

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(steady_tables(n, m))
