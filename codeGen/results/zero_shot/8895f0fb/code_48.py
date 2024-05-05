import sys

def solve():
    T = int(input()) # Read the number of test cases
    for _ in range(T):
        N = int(input()) # Read the maximum number of digits (N)
        total_carries = 0 # Initialize total carries
        total_pairs = 1 # Initialize total pairs
        
        # Generate all possible pairs of N-digit numbers (A and B) 
        for a in range(10**(N-1), 10**N):
            for b in range(a, 10**N):
                # Calculate the total number of carries for this pair
                carry = sum((int(d1) + int(d2)) >= 10 for d1, d2 in zip(str(a)[::-1], str(b)[::-1])) 
                total_carries += carry
                total_pairs *= (N - len(bin(carry)[2:])) # Update the total pairs
        
        # Calculate the average number of carries across all pairs
        expected_value = total_carries / total_pairs
        
        print(f"{expected_value:.6f}") # Print the expected value

if __name__ == "__main__":
    solve()
