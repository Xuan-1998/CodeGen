import sys

def main():
    # Read the number of towns and roads from standard input.
    n = int(input().strip())
    
    # Initialize variables to keep track of the total weight and the maximum weight.
    total_weight = 0
    max_weight = 0
    
    # Read the road descriptions and calculate the total weight and maximum weight.
    for _ in range(n):
        u, v, l = map(int, input().strip().split())
        total_weight += l
        max_weight = max(max_weight, l)
    
    # The minimum possible inconvenience is the total weight minus the maximum weight.
    min_inconvenience = total_weight - max_weight
    
    # Print the result to standard output.
    print(min_inconvenience)

if __name__ == "__main__":
    main()
