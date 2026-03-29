import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    m = list(map(int, sys.stdin.readline().split()))
    
    # Initialize the dictionary to store the frequency of each number in array M
    freq = defaultdict(int)
    for i in range(n):
        freq[m[i]] += 1
    
    # Calculate the number of different ways to create collection V
    total_ways = 1
    for val, count in freq.items():
        if count > 0:
            ways = 1
            for i in range(count):
                ways *= (val - i)
            total_ways *= ways
    
    print(total_ways % (10**9 + 7))

if __name__ == "__main__":
    main()
