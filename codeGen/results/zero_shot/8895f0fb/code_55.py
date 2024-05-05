import sys
from math import comb

def calculate_carries(N):
    # Initialize the total number of carries and the total number of pairs
    total_carries = 0
    total_pairs = 1

    for _ in range(10):  # Loop through each digit (0-9)
        # Calculate the number of carries for this digit
        carries_this_digit = sum(comb(2, k) * (10 ** N) for k in range(N+1))
        
        # Add up the total number of carries and pairs for this test case
        total_carries += carries_this_digit
        total_pairs *= 11

    return total_carries / total_pairs

T = int(input())
for _ in range(T):
    N = int(input())
    print(calculate_carries(N))
