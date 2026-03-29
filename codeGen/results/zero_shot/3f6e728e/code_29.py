import sys
from collections import Counter

def count_sequences(n, m, c):
    # Count the frequency of each radius
    upper_radii = list(map(int, input().split()))
    lower_radii = list(map(int, input().split()))
    
    # Initialize a dictionary to store the frequency of each sequence length
    sequence_counts = {}
    for i in range(c+1):
        sequence_counts[i] = 0
    
    # Count the number of sequences of each length
    for radius in upper_radii:
        if radius > c: continue
        sequence_counts[radius-1] += 1
    for radius in lower_radii:
        if radius > c: continue
        sequence_counts[c-radius] += 1
    
    # Calculate the number of sequences that can be built
    total_sequences = 1
    for count in sequence_counts.values():
        total_sequences *= (count + 1)
    
    return total_sequences % (10**9 + 7)

# Read the input and process each test case
t = int(input())
for _ in range(t):
    n, m, c = map(int, input().split())
    print(count_sequences(n, m, c))
