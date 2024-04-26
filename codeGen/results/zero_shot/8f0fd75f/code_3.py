import sys

def read_input():
    n = int(input().strip())
    x = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))
    return n, x, d

def find_min_durability(n, x, d):
    if n == 0:  # Only two bearing points
        return 0
    
    # Calculate segment lengths
    segment_lengths = [x[i+1] - x[i] for i in range(n+1)]
    
    # Determine collapse points and redistribute load
    for i in range(n):
        if segment_lengths[i] > d[i]:
            if i > 0:
                segment_lengths[i-1] += segment_lengths[i] - d[i]
            if i < n - 1:
                segment_lengths[i+1] += segment_lengths[i] - d[i]
            segment_lengths[i] = d[i]
    
    # Find minimum durability for the new point
    min_durability = max(segment_lengths)
    
    return min_durability

def main():
    n, x, d = read_input()
    min_durability = find_min_durability(n, x, d)
    print(min_durability)

if __name__ == "__main__":
    main()
