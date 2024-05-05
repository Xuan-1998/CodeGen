import sys

def calculate_probability(n):
    # Calculate the total number of configurations possible
    total_configurations = 1
    for _ in range(1, n):
        total_configurations *= 2
    total_configurations %= 998244353
    
    # Calculate the number of valid configurations
    valid_configurations = 1
    for _ in range(1, n-1):
        valid_configurations *= (2 - (_+1)//n)
    valid_configurations %= 998244353
    
    # Return the probability
    return total_configurations // valid_configurations

def main():
    n = int(sys.stdin.readline())
    
    print(calculate_probability(n))

if __name__ == "__main__":
    main()
