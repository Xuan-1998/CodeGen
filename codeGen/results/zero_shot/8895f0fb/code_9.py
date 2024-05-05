import sys

def expected_carries(N):
    # Calculate the probability of non-zero carries for one pair
    p = 0.125
    
    # Calculate the total number of pairs (N choose 2)
    total_pairs = 1 / math.comb(N, 2)
    
    # Calculate the expected value by multiplying the probability and total pairs
    expected_value = p * total_pairs
    
    return expected_value

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(expected_carries(N))
